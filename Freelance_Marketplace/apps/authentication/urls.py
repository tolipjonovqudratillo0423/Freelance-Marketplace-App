from django.urls import path

from apps.authentication.views import (
    AboutMeAPIView, LoginAPIView, RegisterAPIView,
)




urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("about-me/", AboutMeAPIView.as_view(), name="about-me"),
    
]
