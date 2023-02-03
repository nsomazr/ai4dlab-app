from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Learning
from .serializers import LearningModelSerializer
# Create your views here.

class LearningAPIView(APIView):

    def get(self, request):
        learn = Learning.objects.all()
        serializer = LearningModelSerializer(learn, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = LearningModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)


    def learning(request):

        return render(request, template_name='resources/learning.html', context={})