from rest_framework import serializers

from apps.common.models import (
    Country,
    SkillsCategory,
    Skills
)

# =========================================================
# COUNTRY SERIALIZER
# =========================================================
 
class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = [
            "id",
            "name"
        ]
        
        

# =========================================================
# COUNTRY SERIALIZER
# =========================================================
 
class SkillsCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SkillsCategory
        fields = [
            "id",
            "name"
        ]
        
        


# =========================================================
# COUNTRY SERIALIZER
# =========================================================
 
class SkillsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Skills
        fields = [
            "id",
            "category",
            "name"
        ]
        