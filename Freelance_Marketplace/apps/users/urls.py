from django.urls import path

from apps.users.views import (
    LoginAPIView, RegisterAPIView,
    EmailCodeSendAPIView, EmailVerifyAPIView
)



urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("send_code/", EmailCodeSendAPIView.as_view(), name="send_code"),
    path("verify_code/", EmailVerifyAPIView.as_view(), name="verify"),
    
    
]
