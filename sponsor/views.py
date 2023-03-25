from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Sponsor
from django.contrib import messages
from .serializers import SponsorModelSerializer
from .forms import SponsorForm
# Create your views here.

class SponsorAPIView(APIView):

    def get(self, request):
        sponsor = Sponsor.objects.all()
        serializer = SponsorModelSerializer(sponsor, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SponsorModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def sponsor(request):
            sponsors = Sponsor.objects.filter(status=1)
            context = {'sponsors':sponsors}
            return render(request, template_name='about/sponsor.html', context=context)

    def add_sponsor(request):

        if request.method == 'POST' and request.FILES['logo']:

            sponsor_form = SponsorForm(request.POST,request.FILES)

            if sponsor_form.is_valid():
                sponsor_name  = request.POST['sponsor_name']
                website_url = request.POST['website_url']
                description = request.POST['description']
                logo = request.FILES['logo']
                status = 1
                new_sponsor = Sponsor(sponsor_name=sponsor_name, website_url=website_url,description=description, logo=logo, status=status)

                get_objects = Sponsor.objects.filter(sponsor_name=sponsor_name, status=1)
                if get_objects:
                    messages.success(request, "Sponsor already exist.")
                    sponsor_form = SponsorForm()
                    return render(request, template_name='about/add_sponsor.html', context={'sponsor_form':sponsor_form})
                else:
                    new_sponsor.save()
                    sponsors = Sponsor.objects.filter(status=1)
                    context = {'sponsors':sponsors}
                    messages.success(request, "Sponsor successful added." )
                    return render(request,'about/sponsors.html', context=context)

            else:
                print(sponsor_form.errors.as_data())


        sponsor_form = SponsorForm()
        return render(request, template_name='about/add_sponsor.html', context={'sponsor_form':sponsor_form})
    
    def edit_sponsor(request,id):
        sponsor = Sponsor.objects.get(id=id)
        sponsor_form = SponsorForm()
        context = {'sponsor':sponsor, 'sponsor_form':sponsor_form}
        return render(request, template_name='about/edit_sponsor.html', context=context)

    def deactivate_sponsor(request,id):
        sponsor = Sponsor.objects.get(id=id)
        sponsor.status = 0
        sponsor.save()
        return redirect('sponsor:sponsors')

    def delete_sponsor(request,id):
        sponsor = Sponsor.objects.filter(id=id)
        if sponsor:
            sponsor.delete()
            messages.success(request, "Sponsor deleted." )
            return redirect('sponsor:sponsors')
        messages.success(request, "Sponsor doesn't exist." )
        return redirect('sponsor:sponsors')
    

    def sponsors(request):
        sponsors = Sponsor.objects.all()
        context = {'sponsors':sponsors}
        return render(request, template_name='about/sponsors.html', context=context)