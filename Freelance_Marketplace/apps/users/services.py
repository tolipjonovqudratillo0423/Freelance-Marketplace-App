from rest_framework.exceptions import PermissionDenied

from apps.users.models import EmailVerification



# =========================================================
# EMAIL SERVICE
# =========================================================

class EmailService:
    
    @staticmethod
    def is_email_verified(
        code: int,
        user
    ) -> bool:
        
        verify = (
            user.email_verifications
            .order_by("-created_at")
            .first()
        )
        
        if not verify:
            raise PermissionDenied(
                "Verification code not found!"
            )

        if verify.is_expired():
            raise PermissionDenied(
                "Verfication code is expired!"
            )
        
        if verify.attempts >= 6:
            raise PermissionDenied(
                "No attempts left!"
            )
        
        if verify.code != code:
            verify.attempts += 1
            verify.save(update_fields=["attempts"])
            
            raise PermissionDenied(
                "Verification code invalid!"
            )
        
        user.is_verified = True
        user.save(update_fields=["is_verified"])
        
        EmailVerification.objects.filter(
            user=user
        ).delete()
    
        return True
    
    
    
