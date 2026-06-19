from django.urls import path

from apps.projects.views import (
    ProjectAPIView
)
from apps.common.views import (
    CountryAPIView
)
urlpatterns = []


# =========================================================
# PROJECT URLS |||| EVERYONE
# =========================================================        

urlpatterns += [
    path("projects/", ProjectAPIView.as_view(), name="project_list_all"),
    path("countries/", CountryAPIView.as_view(), name="country_list_avaliable"),
]
