from apps.common.models import (
    Country,Skills,SkillsCategory
)

class CommonRepository:
    
    @staticmethod
    def get_active_countries():
        
        countries = (
            Country.objects
            .filter(is_active=True)
        )
        
        return countries
    
    
    @staticmethod
    def get_active_skillscategories():
        
        skillscategories = (
            SkillsCategory.objects
            .filter(is_active=True)
        )
        
        return skillscategories
        
        
    @staticmethod
    def get_active_skills():
        
        skills = (
            Skills.objects
            .filter(is_active=True)
        )
        
        return skills
        
        