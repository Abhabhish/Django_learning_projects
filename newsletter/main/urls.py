from django.urls import path
from . import views

urlpatterns = [
    path('', views.sub_unsub,name='sub_unsub'),
]
