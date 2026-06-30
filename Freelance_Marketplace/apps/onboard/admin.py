from django.contrib import admin

# Register your models here.

from apps.onboard.models import (
    UserProfile, 
    Education,
    Experience,
    FreelancerProfile,
    Portfolio,
)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    
    list_display = ("get_user_username", "image", "phone")
    
    @admin.display(ordering="user__username", description="User")
    def get_user_username(self, obj):
        return obj.user.username if obj.user else "-"



@admin.register(FreelancerProfile)
class FreelancerProfileAdmin(admin.ModelAdmin):
    
    list_display = ("get_freelancer_username", "hourly_rate")
    search_fields = ["profile__user__username"]
    
    @admin.display(ordering="freelancer__username", description="Freelancer")
    def get_freelancer_username(self, obj):
        return obj.profile.user.username if obj.profile else "-"
    


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    
    list_display = ("get_freelancer_username", "title", "link")
    
    @admin.display(ordering="freelancer__username", description="Freelancer")
    def get_freelancer_username(self, obj):
        return obj.freelancer.profile.user.username if obj.freelancer else "-"
  
  

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    
    list_display = ("get_freelancer_username", "level", "name", "faculty")
    search_fields = [ "name"]
    list_filter = ["level"]
    
    @admin.display(ordering="freelancer__username", description="Freelancer")
    def get_freelancer_username(self, obj):
        return obj.freelancer.profile.user.username if obj.freelancer else "-"
  
  

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    
    list_display = ("get_freelancer_username", "company", "position",)
    search_fields = ["company"]
    list_filter = ["position"]
    
    @admin.display(ordering="freelancer__username", description="Freelancer")
    def get_freelancer_username(self, obj):
        return obj.freelancer.profile.user.username if obj.freelancer else "-"
  

