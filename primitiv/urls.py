from django.urls import path
from . import views


urlpatterns = [
    path('view/', views.web1),
    path('', views.home, name = 'home'),
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
]
