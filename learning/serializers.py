from rest_framework import serializers
from .models import Learning

class LearningModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Learning

        # fields = ('__all__')