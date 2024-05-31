from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import *
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import exceptions

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
    
    def get_queryset(self):
        user_id = self.kwargs['pk']
        if user_id == self.request.user.id:
            return User.objects.filter(id=user_id)
        else:
            return User.objects.none()
