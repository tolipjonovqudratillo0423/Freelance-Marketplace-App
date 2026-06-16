from django.urls import path

from apps.bids.views import (
    FreelancerBidAPIView, BidCreateAPIView,
)
from apps.projects.views import (
    ProjectCompleteAPIView
)

urlpatterns = [
    path("bid/", FreelancerBidAPIView.as_view(), name="bid_list_freelancer"),
    path("bid/create", BidCreateAPIView.as_view(), name="bid_create"),
]



# =========================================================
# PROJECT URLS |||| ONLY FREELANCER
# =========================================================        
urlpatterns += [
    path("projects/complete", ProjectCompleteAPIView.as_view(), name="project_complete"),
]

    
