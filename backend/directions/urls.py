from django.urls import path
from .views import *

urlpatterns = [
    path('list/', AllDirectionsAPIView.as_view()),
    path('popular/', AllDetailDirectionsAPIView.as_view()),
    path('<int:pk>/places/', PopularPlacesAPIView.as_view()),
] 