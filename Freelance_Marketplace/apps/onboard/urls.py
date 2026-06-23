from django.urls import path

from apps.onboard.views import (
    CreateFreelancerProfileAPIView,
    CreateProfileAPIView,
    CreateEducationAPIView,
    CreateExperienceAPIView
)

urlpatterns = [
    path("profile/", CreateProfileAPIView.as_view(), name="create_profile"),
    path("freelancer-profile/", CreateFreelancerProfileAPIView.as_view(), name="create_freelancer_profile"),
    path("education/", CreateEducationAPIView.as_view(), name="create_education"),
    path("experience/", CreateExperienceAPIView.as_view(), name="create_experience"),
]