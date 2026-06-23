from django.urls import path

from apps.verification.views import (
    EmailCodeSendAPIView, EmailVerifyAPIView
)




urlpatterns = [
    path("send_code/", EmailCodeSendAPIView.as_view(), name="send_code"),
    path("verify_code/", EmailVerifyAPIView.as_view(), name="verify"),
]
