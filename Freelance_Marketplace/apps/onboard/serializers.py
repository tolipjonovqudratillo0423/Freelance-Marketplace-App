from rest_framework import serializers

from apps.onboard.models import (
    UserProfile,
    FreelancerProfile,
    Experience,
    Education,
    Portfolio
)


#==========================================================
# =========================================================
# ---------------------|| ON_BOARD ||----------------------
# =========================================================
#==========================================================
       
       
#==========================================================
# PROFILE SERIALIZER
#==========================================================

class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        
        model = UserProfile
        
        fields = [
            "user",
            "bio",
            "image",
            "phone",
        ]
        read_only_fields = [
            "user",
        ]
        
    def validate(self, attrs):
        
        validated_data = super().validate(attrs)
        
        bio = validated_data.get("bio", None)
        phone = validated_data.get("phone", None)
        
        if len(bio) < 10:
            
            raise serializers.ValidationError(
                "Bio is too short !"
            )
        
        if len(phone) < 13:
            
            raise serializers.ValidationError(
                "Phone is too short !"
            )
        
        return validated_data
    

#==========================================================
# PROFILE SERIALIZER
#==========================================================

class FreelancerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreelancerProfile
        
        fields = [
            "profile",
            "skills",
            "hourly_rate",
            "resume",
        ]
        
        read_only_fields = [
            "profile",
        ]
    
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        
        hourly_rate = validated_data.get("hourly_rate", None)
       
        if hourly_rate < 0:
            
            raise serializers.ValidationError(
                "Hourly rate can't be negative !"
            )
        
        return validated_data
    


#==========================================================
# PORTFOLIO SERIALIZER
#==========================================================
    
class PortfolioSerializer(serializers.ModelSerializer):

    freelancer = serializers.StringRelatedField()
    
    class Meta:
        model = Portfolio
        fields = [
            "freelancer",
            "title",
            "description",
            "link",
            "image",
        ]
        
        read_only_fields = [
            "freelancer",
        ]
        
    def validate(self, attrs):
        
        validated_data = super().validate(attrs)
        
        freelancer_id = validated_data.get("freelancer_id", None)
        freelancer = validated_data.get("freelancer", None)
        description = validated_data.get("description",None)
        
        if len(description) < 10:
            
            raise serializers.ValidationError(
                "Description is too short !"
            )      
        
        return validated_data
  
            

#==========================================================
# EDUCATION SERIALIZER
#==========================================================
  
class EducationSerializer(serializers.ModelSerializer):
    freelancer = serializers.StringRelatedField()
    
    class Meta:
        model = Education
        fields = [
            "freelancer",
            "level",
            "name",
            "faculty",
            "specialization",
            "end_year"
        ] 
        read_only_fields = [
            "freelancer"
        ] 
    
    def validate(self, attrs):
        validated_data = super().validate(attrs)   
        
        level = validated_data.get("level", None)
        # name = self.validated_data.get("name", None)
        # faculty = self.validated_data.get("faculty", None)
        # specialization = self.validated_data.get("specialization", None)
        # end_year = self.validated_data.get("end_year", None)
        
        if level not in Education.EducationLevel:
            raise serializers.ValidationError(
                "Level is incorrect!"
            )
        
        return validated_data


        
#==========================================================
# EXPERIENCE SERIALIZER
#==========================================================
  
class ExperienceSerializer(serializers.ModelSerializer):
    freelancer = serializers.StringRelatedField()
    
    class Meta:
        model = Experience
        fields = [
            "freelancer",
            "company",
            "position",
            "start_date",
            "end_date",
            "details"
        ] 
        read_only_fields = [
            "freelancer"
        ] 
    
    def validate(self, attrs):
        validated_data = super().validate(attrs)   
        
        details = validated_data.get("details", None)
        
        if len(details) < 10:
            
            raise serializers.ValidationError(
                "Details is too short!"
            )
        
        return validated_data

