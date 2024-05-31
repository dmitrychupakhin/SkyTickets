from rest_framework import serializers
from .models import *
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.backends import TokenBackend

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    confirmation = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirmation')
        write_only_fields = ('confirmation', )
    
    def validate(self, attrs):
        if attrs['password'] != attrs['confirmation']:
            raise serializers.ValidationError("Пароли не совпадают.")
        attrs.pop('confirmation', None)
        return attrs
    
class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'photo', 'date_birth', 'phone_number', 'email')
        
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirmation = serializers.CharField(required=True)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_id'] = user.id
        return token
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user_id'] = self.user.id
        return data
    
class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        token = attrs['refresh']
        token_backend = TokenBackend(algorithm='HS256')
        try:
            token_data = token_backend.decode(token, verify=False)
            user_id = token_data['user_id']
            user = User.objects.get(id=user_id)
        except Exception as e:
            raise serializers.ValidationError('Invalid token')
        
        data = super().validate(attrs)
        data['user_id'] = user_id
        
        return data