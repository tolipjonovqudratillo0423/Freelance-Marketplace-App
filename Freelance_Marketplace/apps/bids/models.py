from django.db import models
from apps.common.models import BaseModel


from django.conf import settings

from apps.projects.models import Project
# Create your models here.




# =========================================================
# BID
# =========================================================

class Bid(BaseModel):
    
    class BidStatus(models.TextChoices):
        NEW = "NEW", "New"
        ACCEPTED = "ACCEPTED", "Accepted"
        DECLINED = "DECLINED", "Declined"
    
    project = models.ForeignKey(
        Project,
        related_name = "bids",
        on_delete = models.CASCADE,
    )
    freelancer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name = "bids",
        on_delete = models.CASCADE,
    )
    
    reply = models.TextField()
    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )
    status = models.CharField(
        choices=BidStatus.choices,
        default=BidStatus.NEW,
        max_length=16,
  
    )
       
    
    
    def __str__(self):
        return f"Freelancer - {self.freelancer.username} ||| Project - {self.project.title} #"
    
    class Meta:
        
        verbose_name = "Bid"
        verbose_name_plural = "Bids"
        
        indexes = [
            models.Index(fields=["project", "freelancer"]), 
            models.Index(fields=["status",])
        ]
        
        constraints = [
            models.UniqueConstraint(
                fields = ["project", "freelancer"],
                name="bid_project_freelancer_unique"
            ),
            models.CheckConstraint(
                condition=models.Q(price__gte=0),
                name="bid_price_positive"
            )
        ]

    