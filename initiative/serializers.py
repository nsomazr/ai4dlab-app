from rest_framework import serializers
from .models import Initiative

class InitiativeModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Initiative

        # fields = ('__all__')