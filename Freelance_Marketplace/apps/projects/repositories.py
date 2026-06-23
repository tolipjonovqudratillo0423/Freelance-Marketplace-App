from apps.projects.models import (
    Project,
)



# =========================================================
# PROJECT REPOSITORY
# =========================================================

class ProjectRepository:
    
    @staticmethod
    def get_all_projects(
        status=Project.StatusChoice.OPEN
    ):
        
        project = (
            Project.objects
            .prefetch_related(
                "required_skills",
            )
            .select_related(
                "client",
                "freelancer",
            )
            .filter(
                status=status
            )
            .order_by(
                "-created_at"
            )
        )
        
        return project
    
    
    @staticmethod
    def get_client_projects(
        user
    ):
        
        project = (
            Project.objects
            .prefetch_related(
                "required_skills",
            )
            .select_related(
                "client",
                "freelancer",
            )
            .filter(
                client=user
            )
            .order_by(
                "-created_at"
            )
        )
        
        return project
    
    
    @staticmethod
    def get_project_for_complete(
        project_id
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
        return project