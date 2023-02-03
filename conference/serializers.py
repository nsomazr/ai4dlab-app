from rest_framework import serializers
from .models import Conference

class ConferenceModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Conference

        fields = ('__all__')