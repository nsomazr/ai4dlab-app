from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Conference
from .serializers import ConferenceModelSerializer
# Create your views here.

class ConferenceAPIView(APIView):

    def get(self, request):
        team = Conference.objects.all()
        serializer = ConferenceModelSerializer(team, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ConferenceModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)
