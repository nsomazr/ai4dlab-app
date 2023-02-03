from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Contact
from .serializers import ContactModelSerializer
# Create your views here.

class ContactAPIView(APIView):

    def get(self, request):
        contact = Contact.objects.all()
        serializer = ContactModelSerializer(contact, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ContactModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def contact(request):

        return render(request, template_name='about/contact-us.html', context={})