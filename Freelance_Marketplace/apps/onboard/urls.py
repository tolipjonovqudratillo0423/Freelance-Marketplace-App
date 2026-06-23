from django.urls import path

from apps.onboard.views import (
    CreateProfileAPIView,
    CreateEducationAPIView,
    CreateExperienceAPIView
)

urlpatterns = [
    path("profile/", CreateProfileAPIView.as_view(), name="create_profile"),
    path("education/", CreateEducationAPIView.as_view(), name="create_education"),
    path("experinece/", CreateExperienceAPIView.as_view(), name="create_experinece"),
]