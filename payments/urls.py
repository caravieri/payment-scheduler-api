from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentScheduleViewSet

router = DefaultRouter()
router.register(r'agendamentos', PaymentScheduleViewSet)  

urlpatterns = [
    path('', include(router.urls)),  
]
