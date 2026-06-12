import secrets
import string

from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.conf import settings




# =========================================================
# REDIRECTOR TO SWAGGER PAGE
# =========================================================

def redirector():
    return redirect("swagger-ui")



# =========================================================
# TOKEN CREATION
# =========================================================

def tokens(user):
    
    refresh = RefreshToken.for_user(user=user)
    
    data = {
        "access_token":str(refresh.access_token),
        "refresh_token":str(refresh)
    }
    
    return data



# =========================================================
# SEND EMAIL FUNCTION
# =========================================================

def send_code(email:str, code:str):
    
    send_mail(
        subject="Verification Code",
        message=f"Your verification code: |{code}|",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )
    


# =========================================================
# CREATE CODE
# =========================================================

def create_code():
    
    code = "".join(secrets.choice(string.digits) for _ in range(6))
    
    return code


# =========================================================
# RESPONSE CREATION
# =========================================================

class ResponseMessage():
    
    @staticmethod
    
    def success(message:str, data:dict =None) -> dict:
        
        response = Response({
            "message":message,
            "data":data,
        }, status=status.HTTP_200_OK)
        
        return response
    
    @staticmethod
    
    def error(message:str, data:dict =None) -> dict:
        
        response = Response({
            "message":message,
            "data":data,
        }, status=status.HTTP_404_NOT_FOUND)
        
        return response
    