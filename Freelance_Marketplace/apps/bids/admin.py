from django.contrib import admin

from apps.bids.models import (
    Bid
)
# Register your models here.

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    
    list_display = ("id","get_freelancer_username", "get_project_title", "status")
    list_filter = ["status",]
    search_fields = ["project__title",]
    list_editable = ["status",]
    
    @admin.display(ordering="freelancer__username", description="Freelancer")
    def get_freelancer_username(self, obj):
        return obj.freelancer.username if obj.freelancer else "-"
    @admin.display(ordering="project__title", description="Project")
    def get_project_title(self, obj):
        return obj.project.title if obj.project else "-"
  

  