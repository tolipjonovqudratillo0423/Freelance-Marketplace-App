from rest_framework import serializers

from apps.projects.models import (
    Project
)


# =========================================================
# PROJECT SHOW SERIALIZER
# =========================================================

class ProjectSerializer(serializers.ModelSerializer):
    freelancer = serializers.StringRelatedField()
    client = serializers.StringRelatedField()
    required_skills = serializers.StringRelatedField(many=True)
    class Meta:
        model = Project
        fields = [
            "id",
            "client",
            "freelancer",
            "required_skills",
            "title",
            "description",
            "min_price",
            "max_price",
            "status",
        ]
        read_only_fields = [
            "id",
            "status",
        ]
        

    
        
# =========================================================
# PROJECT CREATE SERIALIZER
# =========================================================

class ProjectCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = [
            "id",
            "client",
            "freelancer",
            "required_skills",
            "title",
            "description",
            "min_price",
            "max_price",
            "status",
        ]
        read_only_fields = [
            "id",
            "status",
            "client",
            "freelancer"
        ]
        
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        
        return validated_data



    def create(self, validated_data):
        
        required_skills = validated_data.pop("required_skills", [])
    
        project = Project.objects.create(
            **validated_data
        )
        project.required_skills.set(required_skills)
        
        return project

    
    
    def update(self, instance, validated_data):
        
        required_skills = validated_data.pop("required_skills", [])
        
        for attrs, value in validated_data.items():
            setattr(instance, attrs, value)
        instance.save()
        
        if required_skills:
            instance.required_skills.set(required_skills)
            
        return instance
             
        