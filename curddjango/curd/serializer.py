from dataclasses import field
from rest_framework import serializers
from .models import Emp, Issues, Project 

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = '__all__'