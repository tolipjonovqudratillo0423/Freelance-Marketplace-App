from django.urls import path

from apps.projects.views import (
    ProjectAPIView
)

urlpatterns = []


# =========================================================
# PROJECT URLS |||| EVERYONE
# =========================================================        

urlpatterns += [
    path("projects/", ProjectAPIView.as_view(), name="project_list_all"),
]
