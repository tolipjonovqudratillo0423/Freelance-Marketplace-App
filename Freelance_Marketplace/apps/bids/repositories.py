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