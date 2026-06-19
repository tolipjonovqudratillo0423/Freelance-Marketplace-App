from django.contrib import admin

from apps.users.models import (
    User, Skills, SkillsCategory, Country
)
# Register your models here.

# =========================================================
# USER
# =========================================================
admin.site.register(User)
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



# =========================================================
# Skill Category
# =========================================================

@admin.register(SkillsCategory)
class SkillsCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    
@admin.register(Country)
class CountryAdminModel(admin.ModelAdmin):
    list_display = ("id", "name")
    
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"