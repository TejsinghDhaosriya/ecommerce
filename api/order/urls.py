from rest_framework import serializers
from .models import Order

class OrderSerializers(serializers.HyperlinkedSerializers):
    class Meta:
        model =Order
        fields=('user')
        