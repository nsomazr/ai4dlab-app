from rest_framework import serializers
from .models import Publication

class PublicationModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Publication

        fields = ('__all__')