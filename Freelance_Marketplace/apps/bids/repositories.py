from rest_framework.exceptions import ValidationError

from apps.bids.models import Bid

# =========================================================
# BID REPOSITORY
# =========================================================

class BidRepository:
    
    
    @staticmethod
    def get_freelancer_bids(
        freelancer
        ):
        
        bids = (
            Bid.objects
            .select_related(
                "project",
                "freelancer",
            )
            .filter(
                freelancer=freelancer
            )
            .order_by(
                "-created_at"
            )
        )
        
        return bids
    
    @staticmethod
    def get_bid_for_accept(
        bid_id:int
    ):
        
        bid = (
            Bid.objects
            .select_for_update()
            .select_related(
                "freelancer",
                "project",
                "project__client",
            ).filter(
                id=bid_id
            ).first()
        )
        
        return bid
    
    @staticmethod
    def get_project_bids(
        project_id:int
    ):
        bids = list(
            Bid.objects
            .select_related(
                "freelancer"
            )
            .filter(project_id=project_id)
        )
        
        if not bids:
            raise ValidationError("No bids found for this project.")

        return bids
       