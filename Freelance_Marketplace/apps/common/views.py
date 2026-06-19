from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from apps.common.utils import (
    ResponseMessage,
)
from apps.users.serializers import (
    CountrySerializer, Country
)

# Create your views here.


# =========================================================
# COUNTRY APIVIEW
# =========================================================
@extend_schema(
    summary="List of avaliable countries.",
    tags=["Everyone",],
)
class CountryAPIView(APIView):
    
    serializer_class = CountrySerializer
    permission_classes = [AllowAny]
    
    def get(self, request):
        
        country = Country.objects.filter(
            is_active = True
            )
        
        serializer = CountrySerializer(
            country,
            many=True
        )
        
        return ResponseMessage.success(
            message='List of avaliable countries.',
            data=serializer.data           
        )
  