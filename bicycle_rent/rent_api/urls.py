from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, BicycleViewSet, RentalHistoryViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'bicycles', BicycleViewSet)
router.register(r'rentalhistory', RentalHistoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
