from django.urls import path
from . import views

urlpatterns = [
    path('',views.get_translation,name='get_translation')
]