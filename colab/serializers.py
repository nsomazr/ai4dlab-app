from rest_framework import serializers
from .models import Colab

class ColabModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Colab

        fields = ('__all__')