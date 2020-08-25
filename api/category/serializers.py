from rest_framework import serializers

from  .models import Category

class CategorySeriaizers(serializers.Serializer):
    class Meta:
        models = Category
        field = ('name','description')