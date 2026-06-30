from django.db import transaction
from rest_framework.exceptions import PermissionDenied, ValidationError

from apps.bids.models import (
    Bid, Project
)
from apps.bids.repositories import (
    BidRepository
)
from apps.common.utils import (
    send_accept_message_to_email
)

class BidService:
    
    @staticmethod
    @transaction.atomic
    def accept_bid(
        bid_id: int,
        accepted_by
    ):
        
        bid = BidRepository.get_bid_for_accept(
            bid_id=bid_id
        )
        
        if not bid:
            raise ValidationError(
                "Bid not found!"
            )
            
        project = bid.project
        
        if project.client != accepted_by:
            raise PermissionDenied()
        
        if project.status != Project.StatusChoice.OPEN:
            raise ValidationError(
                "Project has already assigned!"
            )
        
        if bid.status != Bid.BidStatus.NEW:
            raise ValidationError(
                "Bid has already processed!"
            )
        
        
        #================LOGIC=================
        
        bid.status = Bid.BidStatus.ACCEPTED
        bid.save(update_fields=["status",])   
        
        project.status = Project.StatusChoice.IN_PROGRESS
        project.freelancer = bid.freelancer
        project.save(update_fields=["status", "freelancer"])
        
        project.bids.filter(
            status=Bid.BidStatus.NEW
        ).exclude(
            id=bid_id
        ).update(
            status=Bid.BidStatus.DECLINED
        )
        try:
            send_accept_message_to_email(
                email=bid.freelancer.email,
                username=bid.freelancer.username,
                project_title=project.title            
            )
        except Exception:
            pass
            
        return project
    

    # @staticmethod
    # @transaction.atomic
    # def complete_bid(
    #     bid_id:int,
    #     completed_by
    # ):
        
    #     bid = (
    #         Bid.objects
    #         .select_for_update()
    #         .select_related(
    #             "freelancer",
    #             "project",
    #         )
    #         .fitler(
    #             id=bid_id,
    #             status=Bid.BidStatus.
    #         )
    #     )