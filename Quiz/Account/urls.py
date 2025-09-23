from django.urls import path
from .views import *


urlpatterns=[
    
    path("",signUp_view,name="signUp"),
    path("login/",login_view,name="login"),
    path("logout/",logout_view,name="logout"),

]