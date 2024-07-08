from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='home'),
    path('<int:product_id>', views.single, name='single')
]