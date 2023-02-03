from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DPortal
from .serializers import DPortalModelSerializer
# Create your views here.

class DPortalAPIView(APIView):

    def get(self, request):
        team = DPortal.objects.all()
        serializer = DPortalModelSerializer(team, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DPortalModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def dportal(request):

        return render(request, template_name='tools/data-portal.html', context={})