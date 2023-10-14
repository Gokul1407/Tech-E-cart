from django.urls import path
from . import views

urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.custom_logout,name='logout'),
    path('forgot_password',views.forgot_password,name='forgot_password')


]    