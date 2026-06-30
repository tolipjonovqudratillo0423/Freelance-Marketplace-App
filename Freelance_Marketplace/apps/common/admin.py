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
    list_display = ("id", "name", "is_active")
    search_fields = ("id", "name",)
    list_editable = ["is_active"]
    


# =========================================================
# Skill Category
# =========================================================

@admin.register(SkillsCategory)
class SkillsCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    search_fields = ["name"]
    list_editable = ["is_active"]
    
    
    class Meta:

        verbose_name = "Skill Category"
        verbose_name_plural = "Skill Categories"
    
    
    
# =========================================================
# COUNTRY
# =========================================================
  
@admin.register(Country)
class CountryAdminModel(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    search_fields = ["name"]
    list_editable = ["is_active"]
    
    
    
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"