from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from tensorflow import keras
import numpy as np
from rest_framework import status
import os

class AllDirectionsAPIView(generics.ListAPIView):
    serializer_class = AllDirSerializer
    queryset = Direction.objects.all()
    
class PopularPlacesAPIView(generics.ListAPIView):
    serializer_class = PlaceSerializer
    queryset = PopularPlace.objects.all()
    
    def get_queryset(self):
        city_id = self.kwargs['pk']
        return PopularPlace.objects.filter(city=city_id)
    
class AllDetailDirectionsAPIView(generics.ListAPIView):
    serializer_class = AllDetailDirSerializer
    queryset = Direction.objects.all()
    
class DirectionPriceAPIView(APIView):
    
    def post(self, request):
        StdNorm = 22683.868561457934
        MeanNorm = 20875.7709068807
        
        date = request.data['date']
        dep_time = request.data['dep_time']
        direction1 = Direction.objects.get(id=request.data['from'])
        direction2 = Direction.objects.get(id=request.data['to'])
        fromm = direction1.city
        to = direction2.city
        clas = request.data['clas']
        time_taken = request.data['time_taken']
        stop = request.data['stop']

        # date / dep_time / from / to / clas / time_taken / stop -> str
        # Вить, это твой запрос
        #response = ["12-03", "09:00", "Mumbai", "Delhi", "economy", "10h 50m", "0"]
        response = [date, dep_time, fromm, to, clas, time_taken, stop]
        # result = price -> int

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
        print(20 * '\n', response)
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
