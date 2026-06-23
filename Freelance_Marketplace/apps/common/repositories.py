from apps.common.models import (
    Country,Skills
)

class CommonRepository:
    
    @staticmethod
    def get_active_countries():
        
        countries = (
            Country.objects
            .filter(is_active=True)
        )
        
        return countries
        