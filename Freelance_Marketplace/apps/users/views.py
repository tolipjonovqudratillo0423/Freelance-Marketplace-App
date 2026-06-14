from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework.serializers import Serializer

from apps.users.serializers import (
    LoginSerializer, RegisterSerializer, 
    EmailVerificationSerializer
    )
from apps.common.utils import (
    tokens, ResponseMessage, 
    send_code, create_code
    )
from apps.users.models import (
    User, EmailVerification,
    Country
    )
from apps.users.services import (
    EmailService
)

# =========================================================
# LOGIN VIEW
# =========================================================
@extend_schema(
    summary="User Login",
    tags=["Auth",],
)
class LoginAPIView(APIView):
    
    serializer_class = LoginSerializer
    
    def post(self, request):
        
        serializer = self.serializer_class(data = request.data)
        
        serializer.is_valid(raise_exception=True)
        
        username = serializer.validated_data.get("username", None)
        password = serializer.validated_data.get("password", None)
        
        user = authenticate(request,username=username, password=password)
        
        if user:
            return ResponseMessage.success("User found ! :)", data=tokens(user))
        
        return ResponseMessage.error("User not found ! :(")
 
 
 
# =========================================================
# REGISTER VIEW
# =========================================================
@extend_schema(
    summary="User Register",
    tags=["Auth",],
)
class RegisterAPIView(APIView):

    serializer_class = RegisterSerializer
    
    def post(self, request):
        
        serializer = self.serializer_class(data = request.data)
        
        serializer.is_valid(raise_exception=True)  
        
        serializer.save()
        
        return ResponseMessage.success(
            "User created, However you should verify your email to unlock more opportunities !",
            serializer.data
        )



# =========================================================
# EMAIL CODE SEND VIEW
# =========================================================
@extend_schema(
    summary="Send VF code to email.",
    tags=["Email Verification",],
)
class EmailCodeSendAPIView(APIView):
    
    
    serializer_class = Serializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        
        user = request.user
        
        if user.is_verified == False:
            code = create_code()
            
            email_code = EmailVerification.objects.filter(
                user = user,
            ).order_by(
                "-created_at"
            ).first()
            if email_code:
                if not email_code.is_expired():
                    return ResponseMessage.error(
                        "Your code have not expired yet !"
                    )
            
            EmailVerification.objects.create(user = user, code = code)
            
            send_code(user.email, code=code)
            return ResponseMessage.success("Code sent ! to :)", data={"email":user.email})
        
        return ResponseMessage.success(
            "You have already verified !",
            data = None,
        )



# =========================================================
# EMAIL CODE VERIFY VIEW
# =========================================================
@extend_schema(
    summary="Verify your code.",
    tags=["Email Verification",],
)
class EmailVerifyAPIView(APIView):
    
    serializer_class = EmailVerificationSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        
        serializer = self.serializer_class(data = request.data)
        
        serializer.is_valid(raise_exception=True)
        
        code = serializer.validated_data.get("code", None)
        
        if not EmailService.is_email_verified(user=request.user, code=code):
            
            return ResponseMessage.error(
                message="Verfication is failed!"
            )
        
        return ResponseMessage.success("Email verified ! :)", data=tokens(request.user))

    