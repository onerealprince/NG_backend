from rest_framework import serializers
from .models import Project, ProjectCard, ProjectEvent

class ProjectCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCard
        fields = '__all__'

class ProjectEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectEvent
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    cards = ProjectCardSerializer(many=True, read_only=True)
    events = ProjectEventSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'
