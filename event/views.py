from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Event
from .serializers import EventModelSerializer
# Create your views here.

class EventAPIView(APIView):

    def get(self, request):
        team = Event.objects.all()
        serializer = EventModelSerializer(team, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EventModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def event(request):

        return render(request, template_name='updates/event.html', context={})