from rest_framework import viewsets
from .serializers import CategorySeriaizers
from .models import Category
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializers_class = CategorySeriaizers
    
    
