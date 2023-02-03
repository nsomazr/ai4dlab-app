from rest_framework import serializers
from .models import Package

class PackageModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Package

        # fields = ('__all__')