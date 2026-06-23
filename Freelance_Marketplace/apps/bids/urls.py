from django.urls import path

from apps.bids.views import (
    FreelancerBidAPIView, BidCreateAPIView,
    ProjectBidsAPIView
)
from apps.projects.views import (
    ProjectCompleteAPIView
)

urlpatterns = [
    path("bid/", FreelancerBidAPIView.as_view(), name="bid_list_freelancer"),
    path("bid/create", BidCreateAPIView.as_view(), name="bid_create"),
    path("project/<int:project_id>/bids", ProjectBidsAPIView.as_view(), name="project_bids"),
]



# =========================================================
# PROJECT URLS |||| ONLY FREELANCER
# =========================================================        
urlpatterns += [
    path("projects/complete", ProjectCompleteAPIView.as_view(), name="project_complete"),
]

    
