from rest_framework import serializers
from .models import Sponsor

class SponsorModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Sponsor

        # fields = ('__all__')