from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Responsibleai
from .serializers import ResponsibleaiModelSerializer
# Create your views here.

class ResponsibleaiAPIView(APIView):

    def get(self, request):
        responsibleai = Responsibleai.objects.all()
        serializer = ResponsibleaiModelSerializer(responsibleai, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ResponsibleaiModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def responsibleai(request):

        return render(request, template_name='research/responsibleai.html', context={})
