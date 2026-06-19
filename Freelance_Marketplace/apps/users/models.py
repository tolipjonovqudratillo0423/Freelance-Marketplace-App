from django.db import models
from apps.common.models import BaseModel
from django.utils import timezone 
from datetime import timedelta

from django.contrib.auth.models import AbstractUser




# =========================================================
# COUNTRY
# =========================================================

class Country(BaseModel):
    
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"



# =========================================================
# SKILLS
# =========================================================

class SkillsCategory(BaseModel):
    
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
  
  
class Skills(BaseModel):
    
    category = models.ForeignKey(
        SkillsCategory,
        related_name="skills",
        on_delete=models.CASCADE
    )
    
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        # ordering = ["created_at"]
       
       
        
# =========================================================
# USER 
# =========================================================


class User(AbstractUser):
    
    class RoleChoice(models.TextChoices):
    
        FREELANCER = "freelancer", "Freelancer"
        CLIENT = "client", "Client"
        
    
    skills = models.ManyToManyField(
        Skills,
        related_name="users"
    )
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
    bio = models.TextField(blank=True, null=True)
    # profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    rating = models.PositiveSmallIntegerField(null=True, blank=True)
    budget = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0,
    )
    is_verified = models.BooleanField(
        default=False
    )
    
    class Meta:
        
        verbose_name = "User"
        verbose_name_plural = "Users"
        
        indexes = [
            models.Index(fields=["role", "rating"]),
            models.Index(fields=["rating", "country"]),
            models.Index(fields=["country", "role"]),
        ]
    


# =========================================================
# VERIFICATION CODE MODEL
# =========================================================

class EmailVerification(BaseModel):
    
    user = models.ForeignKey(
        User,
        related_name="email_verifications",
        on_delete=models.CASCADE
    )
    code = models.CharField(max_length=6)
    attempts = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self):
        return f"Email: {self.user.username} | Code: {self.code}"
    
    def is_expired(self):
        return self.created_at < timezone.now() - timedelta(minutes=5)
    
    