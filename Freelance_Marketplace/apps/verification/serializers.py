from rest_framework import serializers



# =========================================================
# EMAIL VERIFICATION SERIALIZER
# =========================================================
 
class EmailVerificationSerializer(serializers.Serializer):
    
    code = serializers.CharField(
        max_length = 6
    )
    
 