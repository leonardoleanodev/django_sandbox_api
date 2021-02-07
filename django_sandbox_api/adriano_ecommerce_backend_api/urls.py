from django.urls import path
from adriano_ecommerce_backend_api import views

app_name = 'adriano_ecommerce_backend_api'
urlpatterns = [
    path('api/v1/', views.index, name='index'),
]