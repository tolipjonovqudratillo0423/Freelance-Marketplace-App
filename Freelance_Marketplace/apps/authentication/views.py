from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_spectacular.utils import extend_schema

from apps.authentication.serializers import (
    LoginSerializer,
    RegisterSerializer,
    )
from apps.common.utils import (
    tokens,
    ResponseMessage, 
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
            return ResponseMessage.success("User found", data=tokens(user))
        
        return ResponseMessage.error("User not found")
 
 
 
# =========================================================
# REGISTER VIEW
# =========================================================
@extend_schema(
    summary="User Register",
    tags=["Auth",],
)
class RegisterAPIView(APIView):

    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer   
    
    def post(self, request):
        
        serializer = self.serializer_class(data = request.data)
        
        serializer.is_valid(raise_exception=True)  
        
        serializer.save()
        
        return ResponseMessage.success(
            "User created, However you should verify your email to unlock more opportunities !",
        )



#=========================================================
# ABOUT ME VIEW
#=========================================================

class AboutMeAPIView(APIView):
    
    serializer_class = None
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        
        user = request.user
        
        data = {
            "username": user.username,
            "email": user.email,
            "role": user.role,
            "country": user.country.name if user.country else None,
            "is_verified": user.is_verified,
            "is_active": user.is_active,
            "is_onboarded": user.is_onboarded,
            "is_online": user.is_online,
        }
        return ResponseMessage.success("User found", data=data)