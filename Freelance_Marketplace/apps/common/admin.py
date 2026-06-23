from django.contrib import admin

from apps.common.models import (
    Country, SkillsCategory, Skills
)
# Register your models here.


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
    
    
    
# =========================================================
# COUNTRY
# =========================================================
  
@admin.register(Country)
class CountryAdminModel(admin.ModelAdmin):
    list_display = ("id", "name")
    
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"