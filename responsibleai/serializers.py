from rest_framework import serializers
from .models import Responsibleai

class ResponsibleaiModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Responsibleai

        # fields = ('__all__')