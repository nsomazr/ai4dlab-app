from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import News
from .serializers import NewsModelSerializer
from .forms import NewsForm
from django.contrib import messages
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

    def news_list(request):
        news = News.objects.all()
        context = {'news':news}
        return render(request, template_name='updates/news_list.html', context=context)

    def news(request):
        news = News.objects.filter(publish=1, status=1)
        context = {"news": news}
        return render(request, template_name='updates/news.html', context=context)

    def add_news(request):

        if request.method == 'POST' and request.FILES['banner']:

            news_form = NewsForm(request.POST,request.FILES)
            print(f"Body content: {request.POST['body']}")
            if news_form.is_valid():
                title  = request.POST['title']
                body = news_form.cleaned_data['body']
                banner = request.FILES['banner']
                description = request.POST['description']
                publisher = request.POST['publisher']
                thematic_area= request.POST['thematic_area']
                status = 1
                # print(f"Body content: {body}")
                slug = title.replace(' ','-').lower()
                new_news = News(title=title, body=body, banner=banner,description=description, publisher=publisher, status=status, slug=slug, thematic_area=thematic_area)
                get_objects = News.objects.filter(title=title, status=1)
                if get_objects:
                    messages.success(request, "News already exist." )
                    news_form = NewsForm()
                    return render(request, template_name='updates/add_news.html', context={'news_form':news_form})
                else:
                    new_news.save()
                    messages.success(request, "News successful added." )
                    return redirect('news:news-list')
            else:
                print(news_form.errors.as_data())
                
        news_form = NewsForm()
        return render(request, template_name='updates/add_news.html', context={'news_form':news_form})


    def review_news(request,id):
        new = News.objects.get(id=id)
        context = {'new':new}
        return render(request, template_name='updates/review_news.html', context=context)
    
    def read_news(request,slug):
        new = News.objects.get(slug=slug)
        news = News.objects.filter(publish=1, status=1).exclude(slug=slug)
        context = {'new':new, 'news':news}
        return render(request, template_name='updates/news_single.html', context=context)
    
    def view_news(request,id):
        new = News.objects.get(id=id)
        context = {'new':new}
        return render(request, template_name='updates/view_news.html', context=context)
    
    def publish_news(request,id):
            new = News.objects.get(id=id)
            new.publish = 1
            new.save()
            return redirect('news:news-list')
            
    
    def delete_news(request,id):
        new = News.objects.filter(id=id)
        if new:
            new.delete()
            messages.success(request, "News deleted." )
            return redirect('news:news-list')
        messages.success(request, "News doesn't exist." )
        return redirect('news:news-list')