from rest_framework import serializers
from .models import Team, Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'name', 'team', 'on_track_percentage', 'at_risk_percentage', 'off_track_percentage', 'created_at', 'updated_at']

class TeamSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)
    
    class Meta:
        model = Team
        fields = ['id', 'name', 'on_track_percentage', 'at_risk_percentage', 'off_track_percentage', 'created_at', 'updated_at', 'cards'] 