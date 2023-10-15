from django.urls import path, include
from InfoData import views

urlpatterns = [
    path('', views.addEntry)
]
