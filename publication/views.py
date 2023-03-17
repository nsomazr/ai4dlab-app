from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Publication
from .serializers import PublicationModelSerializer
from django.contrib.auth.models import User
from .forms import PublicationForm
from django.contrib import messages
# Create your views here.

class PublicationAPIView(APIView):

    def get(self, request):
        team = Publication.objects.all()
        serializer = PublicationModelSerializer(team, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PublicationModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def publication_list(request):
        publications = Publication.objects.all()
        context = {'publications':publications}
        return render(request, template_name='research/publication_list.html', context=context)

    def publication(request):
        publications = Publication.objects.filter(publish=1, status=1)
        general_count = len(Publication.objects.filter(thematic_area=0))
        health_count = len(Publication.objects.filter(thematic_area=1))
        agriculture_count = len(Publication.objects.filter(thematic_area=2))
        infra_count = len(Publication.objects.filter(thematic_area=3))
        digital_count = len(Publication.objects.filter(thematic_area=4))
        context = {"publications": publications,'general_count':general_count,'health_count':health_count,
                   'agriculture_count':agriculture_count, 'infra_count':infra_count,'digital_count':digital_count}
        return render(request, template_name='research/publication.html', context=context)

    def add_publication(request):

        if request.method == 'POST' and request.FILES['file']:

            publication_form = PublicationForm(request.POST,request.FILES)

            if publication_form.is_valid():
                title  = request.POST['title']
                description = request.POST['description']
                body = request.POST['body']
                header_image = request.FILES['header_image']
                file= request.FILES['file']
                thematic_area= request.POST['thematic_area']
                status = 1
                slug = title.replace(' ','-').lower()
                new_publication = Publication(title=title, description=description, body=body,file=file,thematic_area=thematic_area, header_image=header_image, status=status,publisher_id=request.session['user_id'], slug=slug)
                get_objects = Publication.objects.filter(title=title, status=1)
                if get_objects:
                    messages.success(request, "publication already exist." )
                    publication_form = PublicationForm()
                    return render(request, template_name='research/add_publication.html', context={'publication_form':publication_form})
                else:
                    new_publication.save()
                    messages.success(request, "publication successful added." )
                    return redirect('publication:publication-list')
            else:
                print(publication_form.errors.as_data())
                
        publication_form = PublicationForm()
        return render(request, template_name='research/add_publication.html', context={'publication_form':publication_form})


    def review_publication(request,id):
        publication = Publication.objects.get(id=id)
        context = {'publication':publication}
        return render(request, template_name='research/review_publication.html', context=context)
    
    def read_publication(request,slug):
        publication = Publication.objects.get(slug=slug)
        publisher = User.objects.get(id=publication.publisher_id)
        publisher_posts = Publication.objects.filter(publisher_id=publication.publisher_id).exclude(slug=slug)
        context = {'publication':publication, 'publisher_posts':publisher_posts,'publisher':publisher, 'publisher_posts':publisher_posts[:3]}
        return render(request, template_name='research/publication_single.html', context=context)
    
    def view_publication(request,id):
        publication = Publication.objects.get(id=id)
        context = {'publication':publication}
        return render(request, template_name='research/view_publication.html', context=context)
    
    def publish_publication(request,id):
            publication = Publication.objects.get(id=id)
            publication.publish = 1
            publication.save()
            return redirect('publication:publication-list')
            
    
    def delete_publication(request,id):
        publication = Publication.objects.filter(id=id)
        if publication:
            publication.delete()
            messages.success(request, "publication deleted." )
            return redirect('publication:publication-list')
        messages.success(request, "publication doesn't exist." )
        return redirect('publication:publication-list')