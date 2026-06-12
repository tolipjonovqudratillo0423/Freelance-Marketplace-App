from django.db import transaction
from rest_framework.exceptions import PermissionDenied

from apps.bids.models import (
    Bid, Project
)

class BidService:
    
    @staticmethod
    @transaction.atomic
    def accept_bid(
        bid_id: int,
        accepted_by
    ):
        
        bid = (
            Bid.objects
            .select_for_update()
            .select_related(
                "project",
                "freelancer",
            ).get(id = bid_id)
        )
        
        project = bid.project
        
        if project.client != accepted_by:
            raise PermissionDenied()
        
        if project.status != Project.StatusChoice.OPEN:
            raise PermissionDenied(
                "Project has already assigned!"
            )
        
        if bid.status != Bid.BidStatus.NEW:
            raise PermissionDenied(
                "Bid has already processed!"
            )
        
        
        #================LOGIC=================
        
        bid.status = Bid.BidStatus.ACCEPTED
        bid.save(update_fields=["status",])   
        
        project.status = Project.StatusChoice.IN_PROGRESS
        project.freelancer = accepted_by
        project.save(update_fields=["status", "freelancer"])
        
        project.bids.exclude(id=bid_id).update(status=Bid.BidStatus.DECLINED)
        
        return project