from django.urls import path
from adriano_ecommerce_backend_api import views

app_name = 'adriano_ecommerce_backend_api'
urlpatterns = [
    path('api/v1/', views.index, name='index'), # TODO: remove this when cleaning
    path('api/v1/signin', views.signin, name='index'),
    path('api/v1/user_info', views.user_info), # TODO: remove this when cleaning
]