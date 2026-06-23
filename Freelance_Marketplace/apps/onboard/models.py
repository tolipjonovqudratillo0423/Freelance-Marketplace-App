from django.db import models

from apps.users.models import (
    User
)
from apps.common.models import (
    BaseModel, Skills
)

# =========================================================
# USER PROFILE
# =========================================================

class UserProfile(BaseModel):
    
    user = models.OneToOneField(
        User,
        related_name="profile",
        on_delete=models.CASCADE
    )
    
    bio = models.TextField()
    image = models.ImageField(
        upload_to="user_images/",
        blank=True,
        null=True,
    )
    phone = models.CharField(
        unique=True,
        max_length=14,
    )
   
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "UserProfile"
        verbose_name_plural = "UserProfiles"
        


# =========================================================
# FREELANCER MODEL
# =========================================================

class FreelancerProfile(BaseModel):
    
    profile = models.OneToOneField(
        UserProfile,
        related_name="freelancer_profile",
        on_delete=models.CASCADE
    )
    
    skills = models.ManyToManyField(
        Skills,
        related_name="freelancer_profile",
    )
    resume = models.FileField(
        upload_to="freelancer_resume/",
        blank=True,
        null=True
    )
    hourly_rate = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )
    
    
    def __str__(self):
        return self.profile.user.username  
    
    
  
# =========================================================
# EXPERIANCE MODEL
# =========================================================

class Experience(BaseModel):
    
    freelancer = models.ForeignKey(
        FreelancerProfile,
        related_name="experiences",
        on_delete=models.CASCADE
    )
    
    company = models.CharField(
        max_length = 100
    )
    position = models.CharField(
        max_length=100
    )
    start_date = models.DateField()
    end_date = models.DateField()
    details = models.TextField()
    
    def __str__(self):
        return self.freelancer.profile.user.username
    
    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"
        


# =========================================================
# EDUCATION MODEL
# =========================================================

class Education(BaseModel):
    
    class EducationLevel(models.TextChoices):
        
        Bachelor = 'bachelor', 'Bachelor'
        Master = 'master', 'Master'
        PhD = 'phd' ,'PhD'
     
    freelancer = models.ForeignKey(
        FreelancerProfile,
        related_name="educations",
        on_delete=models.CASCADE
    ) 
    level = models.CharField(
        choices=EducationLevel.choices,
        max_length=20,
    )
    
    name = models.CharField(
        max_length=100
    )
    faculty = models.CharField(
        max_length=100
    )
    specialization = models.CharField(
        max_length=100
    )
    end_year = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.freelancer.profile.user.username
    
    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Educations"
        


# =========================================================
# PORTFOILIO MODEL
# =========================================================

class Portfolio(BaseModel):
    
    freelancer = models.ForeignKey(
        FreelancerProfile,
        related_name="portfolios",
        on_delete=models.CASCADE
    )
    
    title = models.CharField()
    description = models.TextField()
    link = models.URLField()
    image = models.ImageField()

    def __str__(self):
        return self.freelancer.profile.user.username
    
    class Meta:
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolios"
