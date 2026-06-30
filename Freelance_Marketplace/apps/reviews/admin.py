from django.contrib import admin

# Register your models here.
from apps.reviews.models import (
    Review
    
)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("get_project_title",
                    "get_reviewer_username",
                    "get_reviewed_username",
                    "rating")
    
    list_filter = ["rating"]
    list_editable = ["rating"]
    
    @admin.display(ordering="project__title", description="Project")
    def get_project_title(self, obj):
        return obj.project.title if obj.project else "-"
    
    @admin.display(ordering="reviewer__username", description="Reviewer | Client")
    def get_reviewer_username(self, obj):
        return obj.reviewer.username if obj.reviewer else "-"
    
    @admin.display(ordering="reviewed__username", description="Reviewed | Freelancer")
    def get_reviewed_username(self, obj):
        return obj.reviewed.username if obj.reviewed else "-"
    