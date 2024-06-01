from django.contrib import admin
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('addfavorite/', AddFavoriteAPIView.as_view()),
    path('delfavorite/', DelFavoriteAPIView.as_view()),
    path('register/', RegistrationAPIView.as_view()),
    path('<int:id>/favorites/', GetUserFavoriteAPIView.as_view()),
    path('<int:id>/', GetUserByIDAPIView.as_view()),
    path('<int:pk>/edit/', EditProfileAPIView.as_view()),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('password_change/', ChangePasswordAPIView.as_view()),
    path(r'password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
] 