from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('memorama/', memorama, name="memorama"),
    path('crucigrama/', crucigrama, name="crucigrama"),
]
