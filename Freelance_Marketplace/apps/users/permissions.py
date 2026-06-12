from rest_framework.permissions import BasePermission, SAFE_METHODS
from apps.users.models import User

# =========================================================
# CLIENT PERMISSION
# =========================================================

class IsClientOrReadOnly(BasePermission):
    
    """
    This permission is checking the status, role of user
    
    """
    
    def has_permission(self, request, view):
        
        # user = get_user_model().objects.get(id = request.user.id)
        
        return request.user and request.user.is_authenticated and request.user.is_verified and request.user.role == User.RoleChoice.CLIENT
    
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS:
            return True
        
        return obj.client == request.user and request.user.role == User.RoleChoice.CLIENT
        
        

# =========================================================
# CLIENT PERMISSION
# =========================================================

class IsFreelancerOrReadOnly(BasePermission):
    
    def has_permission(self, request, view):
            
        return request.user.is_authenticated and request.user.is_verified and request.user.role == User.RoleChoice.FREELANCER
    
    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS:
            return True
        
        return obj.freelancer == request.user and request.user.role == User.RoleChoice.FREELANCER
    