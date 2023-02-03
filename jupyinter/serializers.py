from rest_framework import serializers
from .models import Jupyinter

class JupyinterModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Jupyinter

        fields = ('__all__')