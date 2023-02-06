from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Partner
from .serializers import PartnerModelSerializer
# Create your views here.

class PartnerAPIView(APIView):

    def get(self, request):
        team = Partner.objects.all()
        serializer = PartnerModelSerializer(team, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PartnerModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def partner(request):

        return render(request, template_name='about/partner.html', context={})

    def add_partner(request):

        return render(request, template_name='about/add_partner.html', context={})

    def partners(request):

        return render(request, template_name='about/partners.html', context={})