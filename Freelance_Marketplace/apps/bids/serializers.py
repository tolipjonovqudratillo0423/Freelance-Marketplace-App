from rest_framework import serializers

from apps.bids.models import (
    Bid, Project
)



# =========================================================
# BID LIST SERIALIZER
# =========================================================

class BidSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    freelancer = serializers.StringRelatedField()
    class Meta:
        
        model = Bid
        fields = [
            "id",
            "project",
            "freelancer",
            "reply",
            "price",
            "status",
        ]
        


# =========================================================
# BID CREATE SERIALIZER
# =========================================================

class BidCreateSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(
        max_digits=15,
        decimal_places=2
    )
    class Meta:
        
        model = Bid
        fields = [
            "project",
            "freelancer",
            "reply",
            "price",
        ]   
        read_only_fields = [
            "freelancer"
        ]
    
    
    def validate(self, attrs):
        validated_data = super().validate(attrs)    
        request = self.context.get("request")
        price = validated_data.get("price", None)
        project = validated_data.get("project", None)
        
        if Bid.objects.filter(project=project, freelancer=request.user).exists():
            raise serializers.ValidationError(
                f"You already placed a bid to {project.title} project!"
            )
        
        if project.status != Project.StatusChoice.OPEN:
            raise serializers.ValidationError(
                "Project status have to be open!"
            )
            
        if price > project.max_price:
            raise serializers.ValidationError(
                F"Price should be lower than {project.max_price}"
            )
        
        if price < project.min_price:
            raise serializers.ValidationError(
                F"Price should be higher than {project.min_price}"
            )
        
        return validated_data
        
    def create(self, validated_data):
        
        bid = Bid.objects.create(**validated_data)
        
        return bid


    def update(self, instance, validated_data):
        
        for attrs, params in validated_data.items():
            setattr(instance, attrs, params)
        instance.save()
        
        return instance

        
# =========================================================
# BID ACCEPT SERIALIZER
# =========================================================

class BidAcceptSerializer(serializers.Serializer):
    
    bid = serializers.IntegerField()
    
    