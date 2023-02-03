from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Call
from .serializers import CallModelSerializer
# Create your views here.

class CallAPIView(APIView):

    def get(self, request):
        calls = Call.objects.all()
        serializer = CallModelSerializer(calls, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CallModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def call(request):

        return render(request, template_name='updates/call.html', context={})