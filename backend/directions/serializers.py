from rest_framework import serializers
from .models import *

class AllDirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ('id', 'city')
        
class AllDetailDirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ('id', 'city', 'photo', 'description')
        
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularPlace
        fields = ('title', 'photo', 'description')