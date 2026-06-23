from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from apps.onboard.serializers import (
    UserProfileSerializer,
    EducationSerializer,
    ExperienceSerializer
)
from apps.common.utils import (
    ResponseMessage
)
from apps.onboard.services import (
    OnBoardService
)



#==========================================================
# PORTFOLIO APIVIEW
#==========================================================
@extend_schema(
    summary="Create User Profile. ",
    tags=["On Boarding",],
) 
class CreateProfileAPIView(APIView):
    
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        
        serializer = self.serializer_class(
            data=request.data
        )
        
        serializer.is_valid(raise_exception=True)
        
        OnBoardService.create_profile_to_user(
            user=request.user,
            serializer=serializer,
        )
        
        return ResponseMessage.success(
            message=F"{request.user.username}'s profile created",
            data=serializer.data
        )
        
        



#==========================================================
# EDUCATION APIVIEW
#==========================================================
@extend_schema(
    summary="Create Freelancer Education. ",
    tags=["On Boarding",],
) 
class CreateEducationAPIView(APIView):
    
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        
        serializer = self.serializer_class(
            data=request.data
        )
        
        serializer.is_valid(raise_exception=True)
        
        OnBoardService.create_education_to_user(
            freelancer=request.user.profile.freelancer_profile,
            serializer=serializer,
        )
        
        return ResponseMessage.success(
            message=F"{request.user.username}'s education created",
            data=serializer.data
        )
        
        



#==========================================================
# EXPERIENCE APIVIEW
#==========================================================
@extend_schema(
    summary="Create Freelancer Experience. ",
    tags=["On Boarding",],
) 
class CreateExperienceAPIView(APIView):
    
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        
        serializer = self.serializer_class(
            data=request.data
        )
        
        serializer.is_valid(raise_exception=True)
        
        OnBoardService.create_experience_to_user(
            freelancer=request.user.profile.freelancer_profile,
            serializer=serializer,
        )
        
        return ResponseMessage.success(
            message=F"{request.user.username}'s experience created",
            data=serializer.data
        )
