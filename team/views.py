from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Team
from .serializers import TeamModelSerializer
# Create your views here.

class TeamAPIView(APIView):

    def get(self, request):
        team = Team.objects.all()
        serializer = TeamModelSerializer(team, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeamModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def team(request):

        return render(request, template_name='about/our-team.html', context={})