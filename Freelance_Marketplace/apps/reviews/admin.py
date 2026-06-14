from django.contrib import admin

# Register your models here.
from apps.reviews.models import (
    Review
    
)

admin.site.register(
    Review
)