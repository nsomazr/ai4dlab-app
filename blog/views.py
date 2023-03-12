from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Blog
from .forms import BlogForm
from .serializers import BlogModelSerializer
from django.contrib import  messages
from django.contrib.auth.models import User
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

    def blog_list(request):
        blogs = Blog.objects.all()
        context = {'blogs':blogs}
        return render(request, template_name='updates/blogs_list.html', context=context)

    def blog(request):
        blogs = Blog.objects.filter(publish=1, status=1)
        context = {"blogs": blogs}
        return render(request, template_name='updates/blog.html', context=context)

    def add_blog(request):

        if request.method == 'POST' and request.FILES['thumbnail']:

            news_form = BlogForm(request.POST,request.FILES)

            if news_form.is_valid():
                title  = request.POST['title']
                description = request.POST['description']
                body = request.POST['body']
                thumbnail = request.FILES['thumbnail']
                header_image = request.FILES['header_image']
                thematic_area= request.POST['thematic_area']
                status = 1
                slug = title.replace(' ','-').lower()
                new_blog = Blog(title=title, description=description, body=body, thumbnail=thumbnail,thematic_area=thematic_area, header_image=header_image, status=status,author_id=request.session['user_id'], slug=slug)
                get_objects = Blog.objects.filter(title=title, status=1)
                if get_objects:
                    messages.success(request, "Blog already exist." )
                    blog_form = BlogForm()
                    return render(request, template_name='updates/add_blog.html', context={'blog_form':blog_form})
                else:
                    new_blog.save()
                    messages.success(request, "Blog successful added." )
                    return redirect('blog:blog-list')
            else:
                print(blog_form.errors.as_data())
                
        blog_form = BlogForm()
        return render(request, template_name='updates/add_blog.html', context={'blog_form':blog_form})


    def review_blog(request,id):
        blog = Blog.objects.get(id=id)
        context = {'blog':blog}
        return render(request, template_name='updates/review_blog.html', context=context)
    
    def read_blog(request,slug):
        blog = Blog.objects.get(slug=slug)
        author = User.objects.get(id=blog.author_id)
        author_posts = Blog.objects.filter(author_id=blog.author_id).exclude(slug=slug)
        author_next = author_prev = None
        if len(author_posts) > 1:
            author_next = author_posts[0]
            author_prev = author_posts[1]
        context = {'blog':blog, 'author':author, 'author_posts':author_posts,'author_next':author_next, 'author_prev':author_prev}
        return render(request, template_name='updates/blog_single.html', context=context)
    
    def view_blog(request,id):
        blog = Blog.objects.get(id=id)
        context = {'blog':blog}
        return render(request, template_name='updates/view_blog.html', context=context)
    
    def publish_blog(request,id):
            blog = Blog.objects.get(id=id)
            blog.publish = 1
            blog.save()
            return redirect('blog:blog-list')
            
    
    def delete_blog(request,id):
        blog = Blog.objects.filter(id=id)
        if blog:
            blog.delete()
            messages.success(request, "Blog deleted." )
            return redirect('blog:blog-list')
        messages.success(request, "Blog doesn't exist." )
        return redirect('blog:blog-list')