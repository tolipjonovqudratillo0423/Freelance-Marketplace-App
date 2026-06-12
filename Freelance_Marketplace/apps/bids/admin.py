from django.contrib import admin

from apps.bids.models import (
    Bid
)
# Register your models here.

admin.site.register([Bid])