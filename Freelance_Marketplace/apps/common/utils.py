import secrets
import string
import os
import logging

from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from email.mime.image import MIMEImage



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

def send_verification_code(email: str, code: str) -> None:
    """
    Sends a branded verification code email to a user from Freeform.
    """
    subject = "Your Freeform Verification Code"
    
    # Context data to pass into your email layout
    context = {
        "company_name": "Freeform",
        "code": code,
    }
    
    # 1. Render the professional HTML version
    html_message = render_to_string("emails/verification_code.html", context)
    
    # 2. Create a clean plain-text fallback version
    plain_message = strip_tags(html_message)
    
    # 3. Send the email securely
    send_mail(
        subject=subject,
        message=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        html_message=html_message,
        fail_silently=False,
    )
    


# =========================================================
# SEND EMAIL FUNCTION
# =========================================================

def send_accept_message_to_email(email: str, username: str, project_title: str) -> None:
    """
    Sends a branded message with an embedded logo image from local templates directory.
    """
    subject = f"Your bid for the project '{project_title}' was accepted! | Freeform"
    
    context = {
        "username": username,
        "project_title": project_title,
    }
    
    # 1. Рендерим HTML
    html_message = render_to_string("emails/bid_accepted.html", context)
    plain_message = strip_tags(html_message)
    
    # 2. Создаем объект письма с корректным аргументом 'to'
    msg = EmailMultiAlternatives(
        subject=subject,
        body=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        to=[email],  # Исправлено
    )
    msg.attach_alternative(html_message, "text/html")
    
    # 3. Прикрепляем картинку (из папки templates/emails/image.jpg)
    image_path = os.path.join(settings.BASE_DIR, "apps","common","templates", "emails", "image.jpg")

    
    try:
        with open(image_path, "rb") as f:
            logo_data = f.read()
            
        mime_image = MIMEImage(logo_data)
        mime_image.add_header("Content-ID", "<logo_image>")
        mime_image.add_header("Content-Disposition", "inline", filename="image.jpg")
        
        msg.attach(mime_image)
    except FileNotFoundError:
        logger = logging.getLogger(__name__)
        logger.warning(f"Logo not found {image_path}.")

    # 4. Отправляем письмо
    msg.send(fail_silently=False)

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
    