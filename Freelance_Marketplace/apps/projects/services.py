from django.db import transaction
from rest_framework.exceptions import ValidationError, PermissionDenied

from apps.projects.models import (
    Project
)
from apps.projects.repositories import (
    ProjectRepository
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
        
        project = ProjectRepository.get_project_for_complete(
            project_id=project_id
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