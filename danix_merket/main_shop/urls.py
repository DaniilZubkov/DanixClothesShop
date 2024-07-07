from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('single/<int:product_id>/', views.single, name='single')
]