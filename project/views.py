from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project
from .forms import ProjectForm
from .serializers import ProjectModelSerializer
from django.contrib import messages
# Create your views here.

class ProjectAPIView(APIView):

    def get(self, request):
        team = Project.objects.all()
        serializer = ProjectModelSerializer(team, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def project_list(request):
        projects = Project.objects.all()
        context = {'projects':projects}
        return render(request, template_name='research/project_list.html', context=context)

    def project(request):
        projects = Project.objects.filter(publish=1, status=1)
        context = {"projects": projects}
        return render(request, template_name='research/project.html', context=context)

    def add_project(request):

        if request.method == 'POST' and request.FILES['thumbnail']:

            project_form = ProjectForm(request.POST,request.FILES)
            print(f"Body content: {request.POST['body']}")
            if project_form.is_valid():
                title  = request.POST['title']
                body = project_form.cleaned_data['body']
                thumbnail = request.FILES['thumbnail']
                header_image = request.FILES['header_image']
                description = request.POST['description']
                thematic_area= request.POST['thematic_area']
                status = 1
                # print(f"Body content: {body}")
                slug = title.replace(' ','-').lower()
                new_project = Project(title=title, body=body, thumbnail=thumbnail, header_image=header_image, description=description,publisher_id=request.session['user_id'], status=status, slug=slug, thematic_area=thematic_area)
                get_objects = Project.objects.filter(title=title, status=1)
                if get_objects:
                    messages.success(request, "Project already exist." )
                    project_form = ProjectForm()
                    return render(request, template_name='research/add_project.html', context={'project_form':project_form})
                else:
                    new_project.save()
                    messages.success(request, "Project successful added." )
                    return redirect('project:project-list')
            else:
                print(project_form.errors.as_data())
                
        project_form = ProjectForm()
        return render(request, template_name='research/add_project.html', context={'project_form':project_form})


    def review_project(request,id):
        project = Project.objects.get(id=id)
        context = {'project':project}
        return render(request, template_name='research/review_project.html', context=context)
    
    def read_project(request,slug):
        project = Project.objects.get(slug=slug)
        projects = Project.objects.filter(publish=1, status=1).exclude(slug=slug)
        context = {'projects':projects, 'project':project}
        return render(request, template_name='research/project_single.html', context=context)
    
    def view_project(request,id):
        project = Project.objects.get(id=id)
        context = {'project':project}
        return render(request, template_name='research/view_project.html', context=context)
    
    def publish_project(request,id):
            project = Project.objects.get(id=id)
            project.publish = 1
            project.save()
            return redirect('project:project-list')
            
    
    def delete_project(request,id):
        project = Project.objects.filter(id=id)
        if project:
            project.delete()
            messages.success(request, "Project deleted." )
            return redirect('project:project-list')
        messages.success(request, "Project doesn't exist." )
        return redirect('project:project-list')