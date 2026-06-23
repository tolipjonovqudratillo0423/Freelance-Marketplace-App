from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator
)

from apps.common.models import BaseModel
from apps.projects.models import (
    Project,
)

User = get_user_model()


# =========================================================
# REVIEWS
# =========================================================

class Review(BaseModel):
    
    project = models.ForeignKey(
        Project,
        related_name = "reviews",
        on_delete=models.CASCADE
    )
    reviewer = models.ForeignKey(
        User,
        related_name = "client_reviews",
        on_delete = models.CASCADE
    )
    reviewed = models.ForeignKey(
        User,
        related_name = "freelancer_reviews",
        on_delete = models.CASCADE,
    )
    rating = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ]
    )
    
    def __str__(self):
        return f"Freelancer {self.reviewed.username} reviewed by {self.reviewer.username} in project {self.project.title}"
    
    class Meta:
        
        constraints = [
            models.UniqueConstraint(
                fields=["project", "reviewed"],
                name="review_per_project"
            )
        ]

