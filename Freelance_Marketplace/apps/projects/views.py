from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.projects.serializers import (
    ProjectSerializer,ProjectCreateSerializer,
    ProjectCompleteSerializer
)
from apps.projects.repositories import (
    ProjectRepository,
)
from apps.common.utils import (
    ResponseMessage
)
from apps.users.permissions import (
    IsClientOrReadOnly, IsFreelancerOrReadOnly
)
from apps.projects.services import (
    ProjectService
)
from apps.projects.filters import (
    ProjectFilter
)
from apps.projects.paginations import (
    StandardProjectPage
)
from apps.bids.serializers import (
    BidSerializer
)

# Create your views here.


# =========================================================
# PROJECT APIVIEW |||| EVERYONE
# =========================================================
@extend_schema(
    summary="All open projects.",
    tags=["Everyone"],
    parameters=[
        OpenApiParameter("min_price", float, description="Min price filter"),
        OpenApiParameter("max_price", float, description="Max price filter"),
        OpenApiParameter("skills", int, description="Skill ID filter"),
        OpenApiParameter("search", str, description="Search by title or description"),
    ]
)
class ProjectAPIView(APIView):
    
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny,]
    
    def get(self, request):
        
        project = ProjectRepository.get_all_projects()
        paginator = StandardProjectPage()
        
        #=====Filter=======================================
        filterset = ProjectFilter(request.GET, queryset=project)
        
        result_page = paginator.paginate_queryset(
            queryset=filterset.qs,
            request=request,
            view=self
        )
        if result_page is not None:
            
            serializer = self.serializer_class(
                result_page,
                many=True
            )
            paginator_resp = paginator.get_paginated_response(
                serializer.data
            )
            return ResponseMessage.success(
                message="Projects",
                data=paginator_resp.data
            )
        
        serializer = self.serializer_class(
            filterset.qs,
            many=True
        )
        return ResponseMessage.success(
            "Projects!", 
            serializer.data
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
 


# =========================================================
# PROJECT COMPLETE APIVIEW |||| ONLY FREELANCER
# =========================================================        
@extend_schema(
    summary="Complete project.",
    tags=["Freelancer",],
)        
class ProjectCompleteAPIView(APIView):
    
    serializer_class = ProjectCompleteSerializer
    permission_classes = [IsAuthenticated, IsFreelancerOrReadOnly]
    
    def post(self, request):
        
        serializer = self.serializer_class(
            data=request.data,
        )
        
        serializer.is_valid(raise_exception=True)
        project_id = serializer.validated_data.get("project_id", None)
        
        
        project = ProjectService.complete_project(
            project_id=project_id,
            freelancer=request.user,
        )
        
        return ResponseMessage.success(
            message="Project completed",
            data={
                "project":project.title, 
                "freelancer":project.freelancer.username, 
                "status":project.status,
                "updated_at":project.updated_at, 
            }
        )
        