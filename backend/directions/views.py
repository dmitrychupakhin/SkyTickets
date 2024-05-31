from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

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