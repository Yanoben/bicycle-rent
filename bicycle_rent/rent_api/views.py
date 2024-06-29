from rest_framework import viewsets
from .models import User, Bicycle, RentalHistory
from .serializers import UserSerializer, BicycleSerializer, RentalHistorySerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BicycleViewSet(viewsets.ModelViewSet):
    queryset = Bicycle.objects.all()
    serializer_class = BicycleSerializer

class RentalHistoryViewSet(viewsets.ModelViewSet):
    queryset = RentalHistory.objects.all()
    serializer_class = RentalHistorySerializer
