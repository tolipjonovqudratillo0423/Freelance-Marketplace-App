from django.contrib import admin

from apps.users.models import (
    User, Skills, SkillsCategory, Country,
    Portfolio,UserProfile,FreelancerProfile,
    Education,Experience,EmailVerification
)
# Register your models here.

# =========================================================
# USER
# =========================================================
admin.site.register([
    User,Portfolio,UserProfile,FreelancerProfile,
    Education,Experience,EmailVerification
    ])
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
    
#     list_display = ("username", "rating", "budget")
#     list_filter = ("skills", "country", "rating",)
#     search_fields = ("username",)
#     # date_hierarchy = "created_at"
#     # ordering = ("-created_at",)
#     fieldsets = (
#         (None, {"fields": ("username", "password")}),
#     )



# =========================================================
# Skills
# =========================================================

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_filter = ("id", "name",)
    search_fields = ("id", "name",)


