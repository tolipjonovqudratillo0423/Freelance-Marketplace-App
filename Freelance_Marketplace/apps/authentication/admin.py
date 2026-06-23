from django.contrib import admin

from apps.users.models import (
    User
)   

# =========================================================
# USER
# =========================================================
admin.site.register([
    User
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

