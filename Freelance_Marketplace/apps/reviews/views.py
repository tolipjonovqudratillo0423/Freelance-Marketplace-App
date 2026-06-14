from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from apps.reviews.repositories import (
    ReviewRepository
)
from apps.reviews.serializers import (
    ReviewSerializer,
    ReviewCreateSerializer,
    ReviewProjectid,
)
from apps.users.permissions import (
    IsClientOrReadOnly
)
from apps.common.utils import (
    ResponseMessage
)

# Create your views here.


# =========================================================
# REVIEWS LIST ALL 
# =========================================================
@extend_schema(
    summary="Review for certain project.",
    tags=["Client"],
)
class ReviewOfProjectAPIView(APIView):
    
    serializer_class = ReviewProjectid
    permission_classes = [IsAuthenticated, IsClientOrReadOnly]
    
    def post(self, request):
        
        serializer = self.serializer_class(
            data=request.data,
            context={"request": request}
        )
        
        serializer.is_valid(raise_exception=True)
        
        review = ReviewRepository.get_by_project(
            reviewer=request.user,
            project_id=serializer.validated_data.get("project_id", None)
        )
        
        serializer = ReviewSerializer(review)
        
        return ResponseMessage.success(
            message="Project review", 
            data=serializer.data    
        )
        
    

# =========================================================
# REVIEWS CREATE
# =========================================================
@extend_schema(
    summary="Create review for certain project.",
    tags=["Client"]
)
class ReviewCreateAPIView(APIView):
    
    serializer_class = ReviewCreateSerializer
    permission_classes = [IsAuthenticated, IsClientOrReadOnly]
    
    def post(self, request):
        
        serializer = self.serializer_class(
            data=request.data,
            context={"request": request}
        )
        
        serializer.is_valid(raise_exception=True)
        
        serializer.save(reviewer=request.user)
        
        return ResponseMessage.success(
            message="Review created! ",
            data=serializer.data
        )