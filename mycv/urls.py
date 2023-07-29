from django.urls import path, include
from .views import *

app_name = 'web'

urlpatterns = [
    path('', index_view, name='index'),
]

