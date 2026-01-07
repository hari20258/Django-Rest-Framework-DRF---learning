from django.urls import path
from . import views

urlpatterns=[
    path('',views.api_home)# localhost url 8000/api/
]