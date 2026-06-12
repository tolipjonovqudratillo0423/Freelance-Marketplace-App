from django.contrib import admin

from apps.projects.models import (
    Project, 
)

# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    
    list_display = ("title", 'status',"get_freelancer_username", "get_client_username")
    list_editable = ["status",]
    
    @admin.display(ordering="freelancer__username", description="Freelancer")
    def get_freelancer_username(self, obj):
        return obj.freelancer.username if obj.freelancer else "-"
    
    @admin.display(ordering="client__username", description="Client")
    def get_client_username(self, obj):
        return obj.client.username if obj.client else "-"