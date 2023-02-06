from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Community
from .serializers import CommunityModelSerializer
# Create your views here.

class CommunityAPIView(APIView):

    def get(self, request):
        comminity = Community.objects.all()
        serializer = CommunityModelSerializer(comminity, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CommunityModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)


    def community(request):

        return render(request, template_name='community/community.html', context={})


    def ai4d_members(request):

        return render(request, template_name='community/ai4d_members.html', context={})

    def girslinai_members(request):

        return render(request, template_name='community/girlsinai_members.html', context={})