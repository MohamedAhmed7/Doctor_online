from rest_framework import serializers
from .models import Reservations
class reservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = '__all__'