from rest_framework import serializers
from .models import Company, Applicant, Resume

class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = '_all_'

class StaffBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffBase
        fields = '_all_'

class managerSerializer(serializers.ModelSerializer):
    class Meta:
        model = manager
        fields = '_all_'
        
class internSerializer(serializers.ModelSerializer):
    class Meta:
        model = intern
        fields = '_all_'
        