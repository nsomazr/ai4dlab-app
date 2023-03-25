from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Workshop
from .serializers import WorkshopModelSerializer
from django.contrib import messages
from .forms import WorkshopForm
# Create your views here.

class WorkshopAPIView(APIView):

    def get(self, request):
        workshop = Workshop.objects.all()
        serializer = WorkshopModelSerializer(workshop, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WorkshopModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def workshop_22(request):
        return render(request, template_name='workshop/2022/index.html', context={})
    
    def workshop_22_organizers(request):
        return render(request, template_name='workshop/2022/organizers.html', context={})
    
    def workshop_22_sessions(request):
        return render(request, template_name='workshop/2022/sessions.html', context={})
    
    def workshop_22_speakers(request):
        return render(request, template_name='workshop/2022/speakers.html', context={})
