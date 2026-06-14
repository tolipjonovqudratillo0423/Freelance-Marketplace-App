from django.urls import path

from apps.reviews.views import (
    ReviewCreateAPIView,
    ReviewOfProjectAPIView,
)

urlpatterns = [
    path("review/", ReviewOfProjectAPIView.as_view(), name="review"),
    path("review/create", ReviewCreateAPIView.as_view(), name="review_create"),
    
]
