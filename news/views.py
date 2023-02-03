from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import News
from .serializers import NewsModelSerializer
# Create your views here.

class NewsAPIView(APIView):

    def get(self, request):
        team = News.objects.all()
        serializer = NewsModelSerializer(team, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = NewsModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def news(request):

        return render(request, template_name='updates/news.html', context={})