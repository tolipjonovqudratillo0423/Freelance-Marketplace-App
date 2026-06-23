from rest_framework import serializers

from apps.common.models import (
    Country
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
        