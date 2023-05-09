from django.urls import path
from . import views

urlpatterns = [
    path('<str:group_name>/', views.index),
    path('test/vtoc/', views.msgfromoutside),
]