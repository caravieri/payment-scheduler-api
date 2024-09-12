from rest_framework import serializers
from .models import PaymentSchedule

class PaymentScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentSchedule 
        fields = '__all__'  
