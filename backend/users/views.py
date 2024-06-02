from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.forms import model_to_dict
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import exceptions
from directions.models import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
        
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
        except exceptions.AuthenticationFailed as e:
            return Response({'Ошибка авторизации': 'Пользователь не найден.'}, status=status.HTTP_400_BAD_REQUEST)
        return response
    
class CustomTokenRefreshView(TokenObtainPairView):
    serializer_class = CustomTokenRefreshSerializer
    
class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            if(serializer.data.get('new_password') == serializer.data.get('confirmation')):
                user = request.user
                if user.check_password(serializer.data.get('old_password')):
                    user.set_password(serializer.data.get('new_password'))
                    user.save()
                    return Response({'message': 'Пароль успешно изменён.'}, status=status.HTTP_200_OK)
                return Response({'error': 'Некорректный старый пароль.'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'error': 'Пароли не совпадают.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetUserByIDAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    
    @swagger_auto_schema(
        operation_description="Получение данных для личного кабинета пользователя",
    )
    def get_object(self):
        user_id = self.kwargs['id']
        if user_id == self.request.user.id:
            return User.objects.get(id=user_id)
        else:
            return None

class EditProfileAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    @swagger_auto_schema(
        operation_description="Редактирование профиля",
    )
    def get_queryset(self):
        user_id = self.kwargs['pk']
        if user_id == self.request.user.id:
            return User.objects.filter(id=user_id)
        else:
            return User.objects.none()
        
class AddFavoriteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_description="Добавление в избранные места пользователя",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'place_id': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='ID места, которое нужно добавить в избранные'
                )
            }
        ),
        responses={200: 'OK'}
    )
    def post(self, request):
        user_id = self.request.user.id
        FavoritePlace = favorite_places.objects.create(
            user = User.objects.get(id=user_id),
            place = PopularPlace.objects.get(id=request.data['place_id'])
        )
        return Response({'message': 'OK'}, status=status.HTTP_200_OK)
    
class DelFavoriteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_description="Удаление из избранных мест пользователя",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'place_id': openapi.Schema(
                    type=openapi.TYPE_INTEGER,
                    description='ID места, которое нужно удалить из избранных'
                )
            }
        ),
        responses={200: 'Удалено из избранных.'}
    )
    def post(self, request):
        
        user_id = self.request.user.id
        place_id = request.data['place_id']
        favorite_place = get_object_or_404(favorite_places, user=user_id, place=place_id)
        favorite_place.delete()
        return Response({'message': 'Удалено из избранных.'}, status=status.HTTP_200_OK)
        
class  GetUserFavoriteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_description="Получение всех избранных мест пользователя по id",
    )
    def get(self, request, id):
        user_id = id
        if user_id == self.request.user.id:
            queryset = favorite_places.objects.filter(user_id=user_id)
            data = []
            for obj in queryset:
                place = PopularPlace.objects.get(id=obj.place.id)
                if(place.photo):
                    place_p = "http://127.0.0.1:8000"+place.photo.url
                else:
                    place_p = None
                temp_place = {
                    'id': place.id,
                    'title': place.title,
                    'photo': place_p,
                    'description': place.description,
                    'city': place.city.city
                }
                data.append(temp_place)
            print(data)
            return Response(data)
            
            
