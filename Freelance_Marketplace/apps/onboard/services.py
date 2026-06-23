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
        data
    ):
        
        phone = data.get("phone", None)
        bio = data.get("bio", None)
        image = data.get("image", None)
        
        user_profile = UserProfile.objects.create(
            user = user,
            phone = phone,
            bio = bio,
            image = image,           
        )
        
        return user_profile
    
    
    @staticmethod
    @transaction.atomic
    def create_freelancer_profile_to_user(
        user_profile,
        data
    ):
        
        skills = data.get("skills", None)
        resume = data.get("resume", None)
        hourly_rate = data.get("hourly_rate", None)
        
        freelancer_profile = FreelancerProfile.objects.create(
            profile = user_profile,
            resume = resume,
            hourly_rate = hourly_rate
        )
        
        freelancer_profile.skills.set(skills)
        
        return freelancer_profile
    
    
    @staticmethod
    @transaction.atomic
    def create_education_to_user(
        freelancer,
        data, 
    ):
        
        level = data.get("level", None)
        name = data.get("name", None)
        faculty = data.get("faculty", None)
        specialization = data.get("specialization", None)
        end_year = data.get("end_year", None)
         
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
        data, 
    ):
        
        company = data.get("company", None)
        position = data.get("position", None)
        start_date = data.get("start_date", None)
        end_date = data.get("end_date", None)
        details = data.get("details", None)
        
        experience = Experience.objects.create(
            freelancer=freelancer,
            position=position,
            company=company,
            start_date=start_date,
            end_date=end_date,
            details=details
        )
        
        return experience
    