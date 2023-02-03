from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Home
from .serializers import HomeModelSerializer
# Create your views here.

class HomeAPIView(APIView):

    def get(self, request):
        team = Home.objects.all()
        serializer = HomeModelSerializer(team, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = HomeModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def home(request):

        return render(request, template_name='home/index.html', context={})
