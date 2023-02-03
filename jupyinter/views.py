from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Jupyinter
from .serializers import JupyinterModelSerializer
# Create your views here.

class JupyinterAPIView(APIView):

    def get(self, request):
        team = Jupyinter.objects.all()
        serializer = JupyinterModelSerializer(team, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = JupyinterModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)


    def jupyinter(request):

        return render(request, template_name='tools/jupyinter.html', context={})