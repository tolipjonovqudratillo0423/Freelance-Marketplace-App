from django.urls import path 

from apps.projects.views import (
    ProjectCreateAPIView,
    ClientProjectAPIView, ProjectCompleteAPIView
)
from apps.bids.views import BidAcceptAPIView

# =========================================================
# PROJECT URLS |||| ONLY CLIENT 
# =========================================================        

urlpatterns = [
    path("projects/all", ClientProjectAPIView.as_view(), name="project_list_client"),
    path("projects/create", ProjectCreateAPIView.as_view(), name="project_create"),
    
]


# =========================================================
# PROJECT URLS |||| ONLY CLIENT 
# =========================================================        
urlpatterns += [
    path("projects/complete", ProjectCompleteAPIView.as_view(), name="project_complete"),
]

# =========================================================
# BID URLS |||| ONLY CLIENT
# =========================================================        

urlpatterns += [
        path("bid/accept", BidAcceptAPIView.as_view(), name="bid_accept"),

]
