from django.urls import path

from apps.bids.views import (
    FreelancerBidAPIView, BidCreateAPIView,
    BidAcceptAPIView
)

urlpatterns = [
    path("bid/", FreelancerBidAPIView.as_view(), name="bid_list_freelancer"),
    path("bid/create", BidCreateAPIView.as_view(), name="bid_create"),
]



    
