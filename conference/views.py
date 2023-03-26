from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Conference
from .serializers import ConferenceModelSerializer
from django.contrib import messages
from .forms import ConferenceForm
# Create your views here.

class ConferenceAPIView(APIView):

    def get(self, request):
        conference = Conference.objects.all()
        serializer = ConferenceModelSerializer(conference, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ConferenceModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def aaiac_23(request):
        return render(request, template_name='conference/aaiac2023/index.html', context={})
    
    
    
    def aaiac_23_call_for_paper(request):
        return render(request, template_name='conference/aaiac2023/call_for_paper.html', context={})
