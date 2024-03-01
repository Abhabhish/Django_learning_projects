from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views

class LogoutViewWithGet(LogoutView):
    # Explicitly allow GET requests alongside POST.
    http_method_names = ['get', 'post', 'options']

    def get(self, request, *args, **kwargs):
        # Call the post method to perform the logout action.
        return self.post(request, *args, **kwargs)

urlpatterns = [
    path('login/',LoginView.as_view(template_name='chat/login.html'),name='login'),
    path('logout/',LogoutViewWithGet.as_view(),name='logout'),
    path('',views.chatting,name= 'chatting')
]
