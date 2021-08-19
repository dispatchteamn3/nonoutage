
from django.urls import path
from .views import *

urlpatterns = [
    path('',Home, name ='home-page'),
    path('Breaker/', Breaker,name='breaker')
]