from django.urls import path
from . import views

urlpatterns = [
    path('',views.nav,name='nav'),
    path('nav',views.nav,name='nav'),
    path('logout',views.logout,name='logout'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup')
]