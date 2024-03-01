from django.urls import path
from . import views


urlpatterns = [
    path('',views.url_shortner,name='url_shortner'),
    path('<str:slug>/',views.redirect_url,name = 'redirect_url')
]
