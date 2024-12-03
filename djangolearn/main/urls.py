from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('vlad/', views.vlad),
    path('yasha/', views.yasha),
    path('tema/', views.tema),
    path('roma/', views.roma),
    path('senya/', views.senya)
]
