from django.urls import path

from apps.auth.views import (
    LoginAPIView, RegisterAPIView,
)




urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("register/", RegisterAPIView.as_view(), name="register"),
    
]
