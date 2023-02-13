from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Home
from .serializers import HomeModelSerializer
from colab.models import Colab
from sponsor.models import Sponsor
from partner.models import Partner
# Create your views here.

class HomeAPIView(APIView):

    def get(self, request):
        team = Home.objects.all()
        serializer = HomeModelSerializer(team, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = HomeModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def home(request):
        colabs = Colab.objects.filter(status=1)
        partners = Partner.objects.filter(status=1)
        sponsors = Sponsor.objects.filter(status=1)
        context = {'partners': partners, 'sponsors':sponsors, 'colabs': colabs}
        return render(request, template_name='home/index.html', context=context)
