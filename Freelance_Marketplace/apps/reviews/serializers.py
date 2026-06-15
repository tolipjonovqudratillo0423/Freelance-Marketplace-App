from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied
from django.db.models import Avg

from apps.reviews.models import (
    Review
)
from apps.projects.models import (
    Project
)
from apps.bids.models import (
    Bid
)



# =========================================================
# REVIEWS SERIALIZER
# =========================================================

class ReviewSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    reviewer = serializers.StringRelatedField()
    reviewed = serializers.StringRelatedField()
    
    
    
    class Meta:
        
        model = Review
        fields = [
            "project",
            "reviewer",
            "reviewed",
            "rating",
        ]
        read_only_fields = [
            "project",
            "reviewer",
            "reviewed",
            "rating",
        ]
        
class ReviewProjectid(serializers.Serializer):
    project_id = serializers.IntegerField()   
    
    def validate_project_id(self, project_id):
        
        request = self.context.get("request", None)
        
        if not Project.objects.filter(id=project_id, client=request.user).exists():
            raise serializers.ValidationError(
                "Project not found!"
            )
        
        return project_id
        
        


# =========================================================
# REVIEWS CREATE
# =========================================================

class ReviewCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Review
        fields = [
            "project",
            "rating",
        ]   
    

    def validate(self, attrs):
        
        validated_data = super().validate(attrs)
        
        project = validated_data.get("project", None)
        reviewed = validated_data.get("reviewed", None)
        rating = validated_data.get("rating", None)
        request = self.context.get("request", None)
        
        if project.client != request.user:
            raise PermissionDenied(
                "You can't review this project!"
            )
        
        
        if project.status != Project.StatusChoice.COMPLETED:
            raise serializers.ValidationError(
                "Project should be completed!"
            )
            
        if Review.objects.filter(project=project, reviewer=request.user).exists():
            raise serializers.ValidationError(
                "You already reviewed this project!"
            )
            
        if not 0 < rating < 6:
            
            raise serializers.ValidationError(
                "Rating is invalid!"
            )
          
        return validated_data

    def create(self, validated_data):
        
        project = validated_data.get("project", None)
        rating = validated_data.get("rating", None)
        request = self.context.get("request", None)
              
        
        review = Review.objects.create(
            project=project, 
            reviewed=project.freelancer,
            rating=rating,
            reviewer=request.user
        )
        
        avg = project.freelancer.freelancer_reviews.aggregate(Avg("rating"))["rating__avg"]
        project.freelancer.rating = round(avg)
        project.freelancer.save(update_fields=["rating"])
        
        return review

    