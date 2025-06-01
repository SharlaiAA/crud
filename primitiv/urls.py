from django.urls import path
from . import views


urlpatterns = [
    path('view/', views.web1),
    path('', views.home, name = 'home'),
    
]
