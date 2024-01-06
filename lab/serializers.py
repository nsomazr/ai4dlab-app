from rest_framework import serializers
from .models import Lab

class LabModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Lab

        # fields = ('__all__')