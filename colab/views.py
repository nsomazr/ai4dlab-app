from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Colab
from .serializers import ColabModelSerializer
# Create your views here.

class ColabAPIView(APIView):

    def get(self, request):
        colabs = Colab.objects.all()
        serializer = ColabModelSerializer(colabs, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ColabModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def colab(request):

        return render(request, template_name='about/colab.html', context={})