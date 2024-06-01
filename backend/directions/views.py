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
    
    def get(self, request):
        current_file_path = os.path.abspath(__file__)
        current_file_path = current_file_path[:-(len("views.py"))][:-len("directions/")] + "model/Avia.h5"
        #model_loaded = keras.models.load_model("../../model/Avia.h5")
        print(current_file_path)
        model_loaded = keras.models.load_model(current_file_path)
        test = np.array([[-1.28, 1.21, 1.14, -0.98, 0.31, 0.17, 0.19, 1]])
        y_pred = model_loaded.predict(test)
        StdNorm = 22683.86
        MeanNorm = 20875.77
        result = y_pred * StdNorm + MeanNorm
        return Response({'result': result}, status=status.HTTP_200_OK)