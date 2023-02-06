from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sponsor
from .serializers import SponsorModelSerializer
# Create your views here.

class SponsorAPIView(APIView):

    def get(self, request):
        sponsor = Sponsor.objects.all()
        serializer = SponsorModelSerializer(sponsor, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SponsorModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def sponsor(request):

        return render(request, template_name='about/sponsor.html', context={})


    def add_sponsor(request):

        return render(request, template_name='about/add_sponsor.html', context={})

    def sponsors(request):

        return render(request, template_name='about/sponsors.html', context={})