from django.urls import path
from .import views
app_name='bankapp'

urlpatterns = [
    path('',views.Regform,name='Regform'),
path('register', views.register,name='register'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    path('add',views.add_userform,name='add_userform'),
]