from rest_framework import serializers
from .models import Workshop

class WorkshopModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Workshop

        fields = ('__all__')