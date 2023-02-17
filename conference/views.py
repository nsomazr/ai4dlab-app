from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Conference
from .serializers import ConferenceModelSerializer
from django.contrib import messages
from .forms import ConferenceForm
# Create your views here.

class ConferenceAPIView(APIView):

    def get(self, request):
        conference = Conference.objects.all()
        serializer = ConferenceModelSerializer(conference, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ConferenceModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def conference(request):
        # conferences = Conference.objects.filter(status=1)
        # context = {'conferences':conferences}
        return render(request, template_name='research/conference.html', context={})

    def add_conference(request):

        if request.method == 'POST' and request.FILES['logo']:

            conference_form = ConferenceForm(request.POST,request.FILES)

            if conference_form.is_valid():
                partner_name  = request.POST['conference_name']
                website_url = request.POST['website_url']
                logo = request.FILES['logo']
                status = 1
                new_partner = Conference(partner_name=partner_name, website_url=website_url, logo=logo, status=status)

                get_objects = Conference.objects.filter(partner_name=partner_name, status=1)
                if get_objects:
                    messages.success(request, "Conference already exist." )
                    conference_form = ConferenceForm()
                    return render(request, template_name='research/add_conference.html', context={'conference_form':conference_form})
                else:
                    new_partner.save()
                    conferences = Conference.objects.filter(status=1)
                    context = {'conferences':conferences}
                    messages.success(request, "Conference successful added." )
                    return render(request,'research/conference.html', context=context)

            else:
                print(conference_form.errors.as_data())


        conference_form = ConferenceForm()
        return render(request, template_name='research/add_conference.html', context={'conference_form':conference_form})
    
    def edit_conference(request,id):
        conference = Conference.objects.get(id=id)
        conference_form = ConferenceForm()
        context = {'conference':conference, 'conference_form':conference_form}
        return render(request, template_name='research/edit_conference.html', context=context)

    def deactivate_conference(request,id):
        conference = Conference.objects.get(id=id)
        conference.status = 0
        conference.save()
        return redirect('conference:conferences')

    def delete_conference(request,id):
        conference = Conference.objects.filter(id=id)
        if conference:
            conference.delete()
            messages.success(request, "Conference deleted." )
            return redirect('conferences:conferences')
        messages.success(request, "Conference doesn't exist." )
        return redirect('conference:conferences')
    

    def conferences(request):
        conferences = Conference.objects.all()
        context = {'conferences':conferences}
        return render(request, template_name='research/conferences.html', context=context)