from rest_framework import serializers
from .models import DPortal,PatientData

class DPortalModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = DPortal

        fields = ('__all__')
        

class PatientDataModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientData
        fields = '__all__'
