from django.contrib import admin

# Register your models here.

from apps.verification.models import (
    EmailVerification
)

@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ("code", "attempts")
    list_filter = ("code", "attempts")
    search_fields = ("code", "attempts")
    
    
    