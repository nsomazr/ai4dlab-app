from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DPortal
from .serializers import DPortalModelSerializer
from .forms import DataForm
from django.contrib import messages
import pandas as pd
from django.contrib.auth.models import User
# Create your views here.

class DPortalAPIView(APIView):

    def get(self, request):
        team = DPortal.objects.all()
        serializer = DPortalModelSerializer(team, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DPortalModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def data_list(request):
        data = DPortal.objects.all()
        context = {'data':data}
        return render(request, template_name='tools/data_list.html', context=context)

    def dportal(request):
        data = DPortal.objects.filter(publish=1, status=1)
        general_count = len(DPortal.objects.filter(thematic_area=0))
        health_count = len(DPortal.objects.filter(thematic_area=1))
        agriculture_count = len(DPortal.objects.filter(thematic_area=2))
        infra_count = len(DPortal.objects.filter(thematic_area=3))
        digital_count = len(DPortal.objects.filter(thematic_area=4))
        context = {"data": data,'general_count':general_count,'health_count':health_count,
                   'agriculture_count':agriculture_count, 'infra_count':infra_count,'digital_count':digital_count}
        return render(request, template_name='tools/data-portal.html', context=context)

    def add_data(request):

        if request.method == 'POST' and request.FILES['file']:

            news_form = DataForm(request.POST,request.FILES)

            if news_form.is_valid():
                name  = request.POST['name']
                description = request.POST['description']
                body = request.POST['body']
                file = request.FILES['file']
                thematic_area= request.POST['thematic_area']
                status = 1
                slug = name.replace(' ','-').lower()
                new_data = DPortal(name=name, description=description, body=body, file=file,thematic_area=thematic_area, status=status,publisher_id=request.session['user_id'], slug=slug)
                get_objects = DPortal.objects.filter(name=name, status=1)
                if get_objects:
                    messages.success(request, "Data already exist." )
                    data_form = DataForm()
                    return render(request, template_name='tools/add_data.html', context={'data_form':data_form})
                else:
                    new_data.save()
                    messages.success(request, "Data successful added." )
                    return redirect('dportal:data-list')
            else:
                print(data_form.errors.as_data())
                
        data_form = DataForm()
        return render(request, template_name='tools/add_data.html', context={'data_form':data_form})


    def review_data(request,id):
        data = DPortal.objects.get(id=id)
        data_file = None
        # if str(data.file).endswith(".xlsx"):
        #     data_file = pd.read_excel(data.file)
        # if str(data.file).endswith(".csv"):
        #     data_file = pd.read_excel(data.file)
        context = {'data':data}
        return render(request, template_name='tools/review_data.html', context=context)
    
    def read_data(request,slug):
        data = DPortal.objects.get(slug=slug)
        data_file = None
        # if str(data.file).endswith(".xlsx"):
        #     data_file = pd.read_excel(data.file)
        # if str(data.file).endswith(".csv"):
        #     data_file = pd.read_excel(data.file)
        #ata_file = data_file.head(5).to_html()
        publisher = User.objects.get(id=data.publisher_id)
        publisher_posts = DPortal.objects.filter(publisher_id=data.publisher_id).exclude(slug=slug)
        context = {'data':data, 'publisher_posts':publisher_posts,'publisher':publisher, 'publisher_posts':publisher_posts[:3]}
        return render(request, template_name='tools/data_single.html', context=context)
    
    def view_data(request,id):
        data = DPortal.objects.get(id=id)
        data_file = None
        # if str(data.file).endswith(".xlsx"):
        #     data_file = pd.read_excel(data.file)
        # if str(data.file).endswith(".csv"):
        #     data_file = pd.read_excel(data.file)
        context = {'data':data}
        return render(request, template_name='tools/view_data.html', context=context)
    
    def publish_data(request,id):
            data = DPortal.objects.get(id=id)
            data.publish = 1
            data.save()
            return redirect('dportal:data-list')
            
    
    def delete_data(request,id):
        data = DPortal.objects.filter(id=id)
        if data:
            data.delete()
            messages.success(request, "Data deleted." )
            return redirect('dportal:data-list')
        messages.success(request, "Data doesn't exist." )
        return redirect('dportal:dportal-list')
