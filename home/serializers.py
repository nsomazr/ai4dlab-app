from rest_framework import serializers
from .models import Home

class HomeModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Home

        # fields = ('__all__')