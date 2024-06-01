from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from tensorflow import keras
import numpy as np
from rest_framework import status
import os
import g4f
from django.core import serializers
from users.models import *

class AllDirectionsAPIView(generics.ListAPIView):
    serializer_class = AllDirSerializer
    queryset = Direction.objects.all()
    
class PopularPlacesAPIView(APIView):
    
    def get(self, request, pk):
        city_id = pk
        if request.user.is_authenticated:
            places = favorite_places.objects.filter(user_id=request.user.id)
            resp = []
            queryset = PopularPlace.objects.filter(city=city_id)
            for obj in queryset:
                if(obj.photo):
                    obj_p = obj.photo
                else:
                    obj_p = None
                temp = {}
                temp['title'] = obj.title
                temp['photo'] = obj_p
                temp['city'] = obj.city.city
                temp['description'] = obj.description
                temp['saved'] = '0'
                for obj2 in places:
                    if(obj2.place_id == obj.id):
                        temp['saved'] = '1'
                        break
                resp.append(temp)
            return Response(resp, status=status.HTTP_200_OK)
        else:
            queryset = PopularPlace.objects.filter(city=city_id)
            serializer = PlaceSerializer(queryset, many=True)
            return Response(serializer.data)
    
class AllDetailDirectionsAPIView(generics.ListAPIView):
    serializer_class = AllDetailDirSerializer
    queryset = Direction.objects.all()
    
class DirectionByIdAPIView(generics.RetrieveAPIView):
    serializer_class = AllDetailDirSerializer
    queryset = Direction.objects.all()
    
    def get_object(self):
        direction_id = self.kwargs['pk']
        return Direction.objects.get(id=direction_id)
        
class DirectionPriceAPIView(APIView):
    
    def post(self, request):
        StdNorm = 22683.868561457934
        MeanNorm = 20875.7709068807
        
        directionfrom = Direction.objects.get(id=request.data['from'])
        directionto = Direction.objects.get(id=request.data['to'])
        fr = directionfrom.city
        to = directionto.city
        fr = fr.replace('Мумбаи', 'Mumbai').replace('Дели','Delhi').replace('Калькутта', 'Kolkata').replace('Хайдарабад', 'Hyderabad').replace('Ченнаи', 'Chennai').replace('Бангалор', 'Bangalore')
        to = fr.replace('Мумбаи', 'Mumbai').replace('Дели','Delhi').replace('Калькутта', 'Kolkata').replace('Хайдарабад', 'Hyderabad').replace('Ченнаи', 'Chennai').replace('Бангалор', 'Bangalore')
        # date / dep_time / from / to / clas / time_taken / stop -> str
        #response = ["12-03", "09:00", "Mumbai", "Delhi", "economy", "10h 50m", "0"]
        response = [request.data['date'], request.data['dep_time'], fr, to, request.data['clas'], request.data['time_taken'], request.data['stop']]
    
        From = ['Mumbai', 'Delhi', 'Hyderabad', 'Chennai', 'Bangalore', 'Kolkata']
        To = ['Mumbai', 'Delhi', 'Hyderabad', 'Chennai', 'Bangalore', 'Kolkata']
        Mean = [283.919857, 781.114409, 2.330489, 2.385270, 0.311351, 732.907093, 0.923924, 3.942571]
        Std = [45.747274, 321.879003, 1.767264, 1.769400, 0.463047, 431.536740, 0.397781, 1.929122]
        response[0] = int(response[0][3:5] + response[0][:2])
        response[1] = int(response[1][:2]) * 60 + int(response[1][3:])
        response[2] = From.index(response[2])
        response[3] = To.index(response[3])
        response[4] = 0 if response[4] == "economy" else 1
        response[5] = int(response[5][:2]) * 60 + int(response[5][4:6])
        response[6] = int(response[6])
        flagOfClas = 1 if response[4] else 0
        for i in range(7):
            response[i] = (response[i] - Mean[i]) / Std[i]
        airline = ['SpiceJet', 'GO FIRST', 'Indigo', 'Air India', 'AirAsia', 'Trujet', 'Vistara', 'StarAir']
        result = []
        current_file_path = os.path.abspath(__file__)
        current_file_path = current_file_path[:-(len("views.py"))][:-len("directions/")] + "model/Avia.h5"
        model = keras.models.load_model(current_file_path)
        for plane in range(len(airline)):
            if flagOfClas and (plane == 3 or plane == 6):
                NormPlane = (plane - Mean[7]) / Std[7]
                test = np.array([[i for i in response + [NormPlane]]])
                y_pred = model.predict(test)
                y_pred = [i for i in y_pred]
                print(y_pred[0][0]* StdNorm + MeanNorm)
                if y_pred[0][0]* StdNorm + MeanNorm > 20_000:
                    result += [[airline[plane], y_pred[0][0] * StdNorm + MeanNorm]]
            elif not(flagOfClas):
                NormPlane = (plane - Mean[7]) / Std[7]
                test = np.array([[i for i in response + [NormPlane]]])
                y_pred = model.predict(test)
                y_pred = [i for i in y_pred]
                if 1200 < y_pred[0][0]* StdNorm + MeanNorm < 25_000:
                    result += [airline[plane] + ": " + str(y_pred[0][0] * StdNorm + MeanNorm)]
        return Response({'result': result}, status=status.HTTP_200_OK)
    
class FactsAPIView(APIView):
    
    def post(self, request):
        direction = Direction.objects.get(id=request.data['direction'])
        badSymbolsForResponse = ['当', '前', '地', '区', '当', '日', '额', '度', '已', '消', '耗', '完', '请', '尝', '试', '更', '换', '网', '络', '环', '境']
        InputMessage = f"Напиши 4 небольших факта о городе {direction} в Индии. Ответ выдавай строго в таком формате с разделителем |, вот так:  тема факта 1|первый факт|тема факта 2|второй факт и тд"
        messages = [{"role": "user", "content": InputMessage}]
        OK = -1
        while OK != 1:
            try:
                StringResponse = gpt(messages)
                if not(any(badSymbol in StringResponse for badSymbol in badSymbolsForResponse)):
                    OK = 1
            except:
                pass
        lines = StringResponse.split('|')
        facts_dict = {}
        for i in range(0, len(lines), 2):
            key = lines[i]
            if i+1 < len(lines):
                facts_dict[key] = lines[i+1]
        return Response(facts_dict, status=status.HTTP_200_OK)
        
def gpt(messages):
    response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            stream=True,
        )
    StringResponse = ''
    for message in response:
        StringResponse += message
    return StringResponse
