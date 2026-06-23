from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from apps.common.utils import (
    ResponseMessage,
)
from apps.common.serializers import (
    CountrySerializer,
    SkillsCategorySerializer,
    SkillsSerializer
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
        


# =========================================================
# SKILLS CATEGORY APIVIEW
# =========================================================
@extend_schema(
    summary="List of avaliable skills categories.",
    tags=["Everyone",],
)
class SkillsCategoryAPIView(APIView):
    
    serializer_class = SkillsCategorySerializer
    permission_classes = [AllowAny]
    
    def get(self, request):
        
        skills_category = CommonRepository.get_active_skillscategories()
        
        serializer = SkillsCategorySerializer(
            skills_category,
            many=True
        )
        
        return ResponseMessage.success(
            message='List of avaliable skills categories.',
            data=serializer.data           
        )
        
        


# =========================================================
# SKILLS APIVIEW
# =========================================================
@extend_schema(
    summary="List of avaliable skills.",
    tags=["Everyone",],
)
class SkillsAPIView(APIView):
    
    serializer_class = SkillsSerializer
    permission_classes = [AllowAny]
    
    def get(self, request):
        
        skills = CommonRepository.get_active_skills()
        
        serializer = SkillsSerializer(
            skills,
            many=True
        )
        
        return ResponseMessage.success(
            message='List of avaliable skills.',
            data=serializer.data           
        )
        
        
        
        
  