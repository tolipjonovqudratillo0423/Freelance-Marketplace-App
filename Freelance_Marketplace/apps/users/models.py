from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.common.models import (
    Country
)
     

# =========================================================   
# ====================================================================
# =================| USER RELATED MODELS | =====================================
# ====================================================================
# =========================================================


# =========================================================
# USER MODEL
# =========================================================

class User(AbstractUser):
    
    class RoleChoice(models.TextChoices):
    
        FREELANCER = "freelancer", "Freelancer"
        CLIENT = "client", "Client"
    
    country = models.ForeignKey(
        Country,
        related_name="users",
        on_delete=models.CASCADE,
        null = True,
        blank = True
    )
    role = models.CharField(
        choices=RoleChoice.choices,
        max_length=16,
        db_index=True,
    )
    balance = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0,
    )
    is_verified = models.BooleanField(
        default=False
    )
    is_onboarded = models.BooleanField(
        default=False
    )
    
    class Meta:
        
        verbose_name = "User"
        verbose_name_plural = "Users"
        
        indexes = [
            models.Index(fields=["country", "role"]),
        ]
    

