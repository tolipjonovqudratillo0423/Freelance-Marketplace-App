from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from apps.authentication.serializers import (
    MyDynamicSerializer,
    )
from apps.verification.serializers import (
    EmailVerificationSerializer
)
from apps.common.utils import (
    tokens, ResponseMessage, 
    send_code, create_code
    )
from apps.verification.models import (
    EmailVerification
    )
from  apps.verification.services import (
    EmailService
)



# =========================================================
# EMAIL CODE SEND VIEW
# =========================================================
@extend_schema(
    summary="Send VF code to email.",
    tags=["Email Verification",],
)
class EmailCodeSendAPIView(APIView):
    
    
    serializer_class = MyDynamicSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        
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
            EmailVerification.objects.update_or_create(
                user=user,
                defaults={
                    "code":code,
                    "attempts":0
                }
            )
            
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
        
        return ResponseMessage.success("Email verified", data=tokens(request.user))

  