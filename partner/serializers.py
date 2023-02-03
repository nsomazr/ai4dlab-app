from rest_framework import serializers
from .models import Partner

class PartnerModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Partner

        fields = ('__all__')