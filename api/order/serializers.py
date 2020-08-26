from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.HyperlinkedSerializers):
    class Meta:
        model =Order
        fields=('user')
        