from django.urls import path ,include
from rest_framework.authtoken import views

from .views import home

urlpatterns = [
     path('',home,name='api.home'),
     path('category/',include('api.category.urls'),name='api.category'),
     path('product/',include('api.product.urls'),name='api.product'),
     path('user/',include('api.user.urls'),name='api.user'),
     path('order/',include('api.order.urls'),name='api.order'),
      path('api-token-auth/', views.obtain_auth_token, name='api_token_auth'),
]
