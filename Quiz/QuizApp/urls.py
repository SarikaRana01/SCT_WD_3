from django.urls import path
from .views import *


urlpatterns=[
    
    path("CategoryDisplay/",CategoryDisplay_view,name="CategoryDisplay"),
    path("submission/<int:id>/",submission_view,name="submission"),

]