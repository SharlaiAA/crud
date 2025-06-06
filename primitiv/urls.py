from django.urls import path
from . import views


urlpatterns = [
    path('view/', views.web1),
    path('', views.home, name = 'home'),
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('register/', views.register_user, name = 'register'),
    path('record/<int:pk>', views.customer_record, name = 'record'),
    path('delete_review/<int:pk>', views.delete_review, name = 'delete_review'),
    path('add_review/', views.add_review, name='add_review'),
    path('all_users/', views.all_users, name = 'all_users'),
]
