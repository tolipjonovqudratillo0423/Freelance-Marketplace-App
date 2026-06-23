from django.db import transaction

from apps.onboard.models import (
    UserProfile,
    Education,
    Experience,
    Portfolio,
    FreelancerProfile
)

# =========================================================
# ONBOARD SERVICE
# =========================================================
    

class OnBoardService:
    
    @staticmethod
    @transaction.atomic 
    def create_profile_to_user(
        user,
        serializer
    ):
        
        phone = serializer.validated_data.get("phone", None)
        bio = serializer.validated_data.get("bio", None)
        image = serializer.validated_data.get("image", None)
        
        user_profile = UserProfile.objects.create(
            user = user,
            phone = phone,
            bio = bio,
            image = image,           
        )
        
        return user_profile
    
    
    @staticmethod
    @transaction.atomic
    def create_education_to_user(
        freelancer,
        serializer, 
    ):
        
        level = serializer.validated_data.get("level", None)
        name = serializer.validated_data.get("name", None)
        faculty = serializer.validated_data.get("faculty", None)
        specialization = serializer.validated_data.get("specialization", None)
        end_year = serializer.validated_data.get("end_year", None)
         
        education = Education.objects.create(
            freelancer=freelancer,
            level=level,
            name=name,
            faculty=faculty,
            specialization=specialization,
            end_year=end_year,
        )
        
        return education
    
    
    
    @staticmethod
    @transaction.atomic
    def create_experience_to_user(
        freelancer,
        serializer, 
    ):
        
        company = serializer.validated_data.get("company", None)
        position = serializer.validated_data.get("position", None)
        start_date = serializer.validated_data.get("start_date", None)
        end_date = serializer.validated_data.get("end_date", None)
         
        experience = Experience.objects.create(
            freelancer=freelancer,
            position=position,
            company=company,
            start_date=start_date,
            end_date=end_date,
        )
        
        return experience
    