import string

from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

from apps.users.models import User, Country



# =========================================================
# LOGIN SERIALIZER
# =========================================================

class LoginSerializer(serializers.Serializer):
    
    username = serializers.CharField(
        max_length = 100,
        required = True,
    )
    password = serializers.CharField(
        max_length = 100,
        required = True
    )
    
           
        
# =========================================================
# REGISTER SERIALIZER
# =========================================================

class RegisterSerializer(serializers.Serializer):
    
    username = serializers.CharField(
        max_length = 100
    )
    email = serializers.EmailField(
        max_length = 120
    )
    password = serializers.CharField(
        max_length = 120
    )
    confirm_password = serializers.CharField(
        max_length = 120
    )
    role = serializers.CharField(
        max_length = 16
    )
    country = serializers.IntegerField()
    
    
    def validate_password(self, value):
        try: 
            validate_password(value)
        except DjangoValidationError as err:  
            raise serializers.ValidationError(f"{err}")

        return value
    
    def validate(self, attrs):
        
        validated_data = super().validate(attrs)
        
        username = validated_data.get("username", None)
        password1 = validated_data.get("password", None)
        password2 = validated_data.get("confirm_password", None)
        email = validated_data.get("email", None)
        role = validated_data.get("role", None)
        country = validated_data.get("country", None)
        
        if User.objects.filter(username = username).exists():
            
            raise serializers.ValidationError(
                "Account can't be created"
            )
        
        if User.objects.filter(email = email).exists():
            
            raise serializers.ValidationError(
                "Account can't be created"
            )
        
        if not Country.objects.filter(id=country).exists():
            
            raise serializers.ValidationError(
                "Coutnry doesn't exists ! :("
            )
            
        if len(username) < 3:
            
            raise serializers.ValidationError(
                "Username is too short ! :("
            )
        
        if password1 != password2:
            raise serializers.ValidationError(
                "Paswords don't match ! :("
            )
        
        if role not in (
            User.RoleChoice.FREELANCER,
            User.RoleChoice.CLIENT
        ):
            raise serializers.ValidationError(
                "Role is not found !"
            )
        
        return validated_data
        
        

# =========================================================
# EMAIL VERIFICATION SERIALIZER
# =========================================================
 
class EmailVerificationSerializer(serializers.Serializer):
    
    code = serializers.CharField(
        max_length = 6
    )
    