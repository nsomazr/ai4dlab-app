from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Package
from .serializers import PackageModelSerializer
# Create your views here.

class PackageAPIView(APIView):

    def get(self, request):
        package = Package.objects.all()
        serializer = PackageModelSerializer(package, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PackageModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)


    def package(request):

        return render(request, template_name='resources/package.html', context={})