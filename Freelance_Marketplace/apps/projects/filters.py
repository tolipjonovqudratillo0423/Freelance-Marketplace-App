from django_filters import rest_framework as filter
from django_filters.rest_framework import DjangoFilterBackend
from django.db import models


from apps.projects.models import (
    Project
)

class ProjectFilter(filter.FilterSet):
    
    min_price = filter.NumberFilter(
        field_name="min_price",
        lookup_expr="gte"
    )
    max_price = filter.NumberFilter(
        field_name="max_price",
        lookup_expr="lte"
    )
    required_skills = filter.NumberFilter(
        field_name="required_skills__id"
    )
    search = filter.CharFilter(
        method="search_filter"
    )
    
    def search_filter(self, queryset, name, value):
        return queryset.filter(
            models.Q(title__icontains=value) |
            models.Q(description__icontains=value)
        )
        
    class Meta:
        model = Project
        fields = [
            "min_price",
            "max_price",
            "required_skills",
        ]