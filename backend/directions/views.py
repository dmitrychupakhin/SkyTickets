from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
#from tensorflow import keras
#import numpy as np

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
        model_loaded = keras.models.load_model("../../model/modelForEconomy")
        test = np.array([[-1.28, 1.21, 1.14, -0.98, 0.31, 0.17, 0.19]])
        y_pred = model_loaded.predict(test)
        StdNorm = 3.74
        MeanNorm = 6.57
        print(y_pred * StdNorm + MeanNorm)