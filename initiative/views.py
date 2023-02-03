from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Initiative
from .serializers import InitiativeModelSerializer
# Create your views here.

class InitiativeAPIView(APIView):

    def get(self, request):
        team = Initiative.objects.all()
        serializer = InitiativeModelSerializer(team, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = InitiativeModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def initiative(request):

        return render(request, template_name='research/initiative.html', context={})
