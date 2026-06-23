from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from apps.common.utils import (
    ResponseMessage,
)
from apps.common.serializers import (
    CountrySerializer
)
from apps.common.repositories import(
    CommonRepository
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
        
        country = CommonRepository.get_active_countries()
        
        serializer = CountrySerializer(
            country,
            many=True
        )
        
        return ResponseMessage.success(
            message='List of avaliable countries.',
            data=serializer.data           
        )
        
        
        
        
  