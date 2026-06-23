from math import ceil
from django.db import transaction
from django.db.models import Avg

from apps.reviews.models import (
    Review
)



# =========================================================
# REVIEW SERVICE
# =========================================================

class ReviewService:
    
    @staticmethod
    @transaction.atomic
    def create_review(
        project,
        rating,
        reviewer
    ):
            
        review = Review.objects.create(
            project=project, 
            reviewed=project.freelancer,
            rating=rating,
            reviewer=reviewer
        )
        
        avg = project.freelancer.freelancer_reviews.aggregate(Avg("rating"))["rating__avg"]
        if avg is not None:
            project.freelancer.rating = ceil(avg)
            project.freelancer.save(update_fields=["rating"])
        
        return review

