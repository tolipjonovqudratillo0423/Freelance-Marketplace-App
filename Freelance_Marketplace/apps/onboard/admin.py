from django.contrib import admin

# Register your models here.

from apps.onboard.models import (
    UserProfile, 
    Education,
    Experience,
    FreelancerProfile,
    Portfolio,
)

admin.site.register([
    UserProfile, 
    Education,
    Experience,
    FreelancerProfile,
    Portfolio,
])