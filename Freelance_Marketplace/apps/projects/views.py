from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.projects.serializers import (
    ProjectSerializer,ProjectCreateSerializer
)
from apps.projects.repositories import (
    ProjectRepository,
)
from apps.common.utils import (
    ResponseMessage
)
from apps.users.permissions import (
    IsClientOrReadOnly
)
# Create your views here.


# =========================================================
# PROJECT APIVIEW |||| EVERYONE
# =========================================================
@extend_schema(
    summary="All open projects.",
    tags=["Everyone",],
)
class ProjectAPIView(APIView):
    
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny,]
    
    def get(self, request):
        
        project = ProjectRepository.get_all_projects()
        
        serializer = self.serializer_class(
            project,
            many=True
            )
        
        
        return ResponseMessage.success(
            message="Projects",
            data=serializer.data
        )
        
        
        
# =========================================================
# PROJECT CREATE APIVIEW |||| ONLY CLIENT
# =========================================================        
@extend_schema(
    summary="Create Project.",
    tags=["Client",],
)     
class ProjectCreateAPIView(APIView):
    
    serializer_class = ProjectCreateSerializer
    permission_classes = [IsAuthenticated, IsClientOrReadOnly]  
    
    def post(self, request):
        
        serializer = self.serializer_class(data = request.data)
        
        serializer.is_valid(raise_exception=True)
        
        # serializer.save(commit=False)     
        serializer.save(client = request.user)
          
        return ResponseMessage.success(
            message="Project created! ",
            data=serializer.data
        )
   


# =========================================================
# CLIENT'S PROJECT APIVIEW |||| ONLY CLIENT
# =========================================================        
@extend_schema(
    summary="Only certain client's projects.",
    tags=["Client",],
) 
class ClientProjectAPIView(APIView):
    
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsClientOrReadOnly]
    
    def get(self, request):
        
        project = ProjectRepository.get_client_projects(
            user=request.user
        )
        
        serializer = self.serializer_class(
            project,
            many=True
        )
        
        return ResponseMessage.success(
            message=F"{request.user.username}'s projects!",
            data=serializer.data
        )
