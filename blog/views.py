from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogModelSerializer
# Create your views here.

class BlogAPIView(APIView):

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogModelSerializer(blogs, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BlogModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def blog(request):

        return render(request, template_name='updates/blog.html', context={})

    
    def add_blog(request):

        return render(request, template_name='updates/add_blog.html', context={})

    def blogs(request):

        return render(request, template_name='updates/blog_list.html', context={})