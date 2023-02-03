from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Publication
from .serializers import PublicationModelSerializer
# Create your views here.

class PublicationAPIView(APIView):

    def get(self, request):
        team = Publication.objects.all()
        serializer = PublicationModelSerializer(team, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PublicationModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def publication(request):

        return render(request, template_name='research/publication.html', context={})