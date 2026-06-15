from django.db import transaction
from rest_framework.exceptions import ValidationError, PermissionDenied

from apps.projects.models import (
    Project
)


# =========================================================
# PROJECT SERVICE
# =========================================================

class ProjectService:
    
    @staticmethod
    @transaction.atomic
    def complete_project(
        freelancer,
        project_id,
    ):
        
        project = (
            Project.objects
            .select_for_update()
            .select_related(
                "freelancer"
            )
            .filter(
                id=project_id
            ).first()
        )
        
        if not project:
            raise ValidationError("Project does not exist!")
        
        if project.freelancer != freelancer:
            raise PermissionDenied("You are not the freelancer!")
        
        if project.status != Project.StatusChoice.IN_PROGRESS:
            raise ValidationError("Project should be in progress!")
        
        project.status = Project.StatusChoice.COMPLETED
        project.save(update_fields=["status"])
        
        return project