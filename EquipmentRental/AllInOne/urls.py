from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, EquipmentViewSet, RentalViewSet

router = DefaultRouter()
router.register('customer', CustomerViewSet, basename='customer')

# РЕГИСТРИРУЕМ НОВЫЕ ЭНДПОИНТЫ ТУТ:
router.register('equipment', EquipmentViewSet, basename='equipment')
router.register('rental', RentalViewSet, basename='rental')

urlpatterns = [
    path('api/', include(router.urls)),
]