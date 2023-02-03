from rest_framework import serializers
from .models import DPortal

class DPortalModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = DPortal

        fields = ('__all__')