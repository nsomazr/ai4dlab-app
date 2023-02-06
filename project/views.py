from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .serializers import ProjectModelSerializer
# Create your views here.

class ProjectAPIView(APIView):

    def get(self, request):
        team = Project.objects.all()
        serializer = ProjectModelSerializer(team, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def project(request):

        return render(request, template_name='research/project.html', context={})
    
    def add_project(request):

        return render(request, template_name='research/add_project.html', context={})

    def projects(request):

        return render(request, template_name='research/project_list.html', context={})