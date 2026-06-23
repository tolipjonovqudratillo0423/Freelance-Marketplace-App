from rest_framework.views import APIView
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from apps.bids.repositories import (
    BidRepository
)
from apps.bids.services import (
    BidService
)
from apps.bids.serializers import (
    BidSerializer, BidCreateSerializer,
    BidAcceptSerializer
)
from apps.common.utils import (
    ResponseMessage
)
from apps.users.permissions import (
    IsFreelancerOrReadOnly, IsClientOrReadOnly
)
# Create your views here.



# =========================================================
# BID LIST GET APIVIEW |||| ONLY FREELACNER
# =========================================================
@extend_schema(
    summary="Freelancer Bids",
    tags=["Freelancer",],
) 
class FreelancerBidAPIView(APIView):
    
    permission_classes = [IsAuthenticated, IsFreelancerOrReadOnly]
    serializer_class = BidSerializer
    
    def get(self, request):
        
        bids = BidRepository.get_freelancer_bids(freelancer=request.user)
        
        serializer = self.serializer_class(bids, many=True)
        
        return ResponseMessage.success(
            message="Bids",
            data=serializer.data
        )
        
        
      
# =========================================================
# BID CREATE APIVIEW |||| ONLY FREELACNER
# =========================================================
@extend_schema(
    summary="Bid create",
    tags=["Freelancer",],
) 
class BidCreateAPIView(APIView):
    
    permission_classes = [IsAuthenticated, IsFreelancerOrReadOnly]
    serializer_class = BidCreateSerializer
    
    def post(self, request):
        
        user = request.user
        
        serializer = self.serializer_class(
            data = request.data,
            context = {
                'request': request
                }
            )
        
        
        serializer.is_valid(
            raise_exception=True
        )
          
        try: 
            serializer.save(freelancer = user)
            return ResponseMessage.success(
                message="Bid Created",
                data=serializer.data
            )
        except IntegrityError:
            
            return ResponseMessage.error(
                message="You already placed a bid",
                data=serializer.data
            )
        
        
        
    
    
# =========================================================
# BID ACCEPT APIVIEW |||| ONLY CLIENT
# =========================================================
@extend_schema(
    summary="Bid Accept",
    tags=["Client",],
) 
class BidAcceptAPIView(APIView):
    
    serializer_class = BidAcceptSerializer
    permission_classes = [IsAuthenticated, IsClientOrReadOnly]
    
    def post(self, request):
        
        serializer = self.serializer_class(
            data=request.data
        )
        
        serializer.is_valid(
            raise_exception=True
        )
        
        project = BidService.accept_bid(
            bid_id=serializer.validated_data.get("bid", None),
            accepted_by=request.user
        )
        
        return ResponseMessage.success(
        message="Bid accepted!",
        data={
            "project": project.title,
            "status": project.status,
            "freelancer": project.freelancer.username
        }
)