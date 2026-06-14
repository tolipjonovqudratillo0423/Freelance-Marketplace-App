from apps.reviews.models import (
    Review
)


# =========================================================
# REVIEWS REPOSITORY
# =========================================================

class ReviewRepository:
    
    
    @staticmethod
    def get_by_project(
        reviewer,
        project_id, 
    )-> Review: 
        
        review = (
            Review.objects
            .select_related(
                "reviewer",
                "reviewed",
                "project",
            ).filter(
                reviewer = reviewer,
                project_id = project_id
            )
        )
        
        return review