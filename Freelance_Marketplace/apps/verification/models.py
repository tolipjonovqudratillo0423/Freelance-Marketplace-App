from django.db import models
from django.utils import timezone 
from datetime import timedelta

from apps.common.models import (
    BaseModel
)
from apps.users.models import (
    User
)
     
# Create your models here.

# =========================================================
# VERIFICATION CODE MODEL
# =========================================================

class EmailVerification(BaseModel):
    
    user = models.ForeignKey(
        User,
        related_name="email_verifications",
        on_delete=models.CASCADE
    )
    code = models.CharField(max_length=6, db_index=True)
    attempts = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self):
        return f"Email: {self.user.username} | Code: {self.code}"
    
    def is_expired(self):
        return self.created_at < timezone.now() - timedelta(minutes=5)
    
    