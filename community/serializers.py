from rest_framework import serializers
from .models import UDOMAI
from .models import AI4D
class UDOMAIModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = UDOMAI

        # fields = ('__all__')
        
class AI4DModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = AI4D

        # fields = ('__all__')