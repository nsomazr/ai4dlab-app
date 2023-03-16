from rest_framework import serializers
from .models import UDOMAI

class UDOMAIModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = UDOMAI

        # fields = ('__all__')