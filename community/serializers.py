from rest_framework import serializers
from .models import Community

class CommunityModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Community

        # fields = ('__all__')