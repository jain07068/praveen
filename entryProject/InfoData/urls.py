from django.urls import path, include
from InfoData import views

urlpatterns = [
    path('info/', views.addEntry),
    path('', views.addEntry)
]
