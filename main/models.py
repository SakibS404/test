from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    on_track_percentage = models.IntegerField()
    at_risk_percentage = models.IntegerField()
    off_track_percentage = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Card(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='cards')
    on_track_percentage = models.IntegerField()
    at_risk_percentage = models.IntegerField()
    off_track_percentage = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.team.name}"
