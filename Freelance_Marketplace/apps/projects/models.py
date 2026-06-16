from django.db import models
from apps.common.models import BaseModel
from django.conf import settings
from apps.users.models import Skills


# =========================================================
# PROJECT
# =========================================================

class Project(BaseModel):
    
    class StatusChoice(models.TextChoices):
        
        OPEN = "open", "OPEN"
        IN_PROGRESS = "in_progress","IN_PROGRESS"
        COMPLETED = "completed","COMPLETED"
        
        
    
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="client_projects",
        on_delete=models.CASCADE,
    )
    freelancer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="freelancer_projects",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    required_skills = models.ManyToManyField(
        Skills,
        related_name="projects",
    )
    
    title = models.CharField(
        max_length=100
    )
    description = models.TextField()
    min_price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )
    max_price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )
    status = models.CharField(
        choices=StatusChoice.choices,
        max_length=16,
        default=StatusChoice.OPEN,
        db_index=True
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        
        verbose_name = "Project"
        verbose_name_plural = "Projects"

        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["status", "client"]),
        ]
        

        constraints = [
            models.CheckConstraint(
                # Заменили check= на condition=
                condition=models.Q(max_price__gte=models.F("min_price")), 
                name="project_price_valid"
            )]
        
        
    
    