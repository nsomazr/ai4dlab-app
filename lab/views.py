from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Lab
from .serializers import LabModelSerializer
# Create your views here.

class LabAPIView(APIView):

    def get(self, request):
        lab = Lab.objects.all()
        serializer = LabModelSerializer(lab, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = LabModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def lab(request):

        return render(request, template_name='about/lab.html', context={})
