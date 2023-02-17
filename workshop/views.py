from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Workshop
from .serializers import WorkshopModelSerializer
from django.contrib import messages
from .forms import WorkshopForm
# Create your views here.

class WorkshopAPIView(APIView):

    def get(self, request):
        workshop = Workshop.objects.all()
        serializer = WorkshopModelSerializer(workshop, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WorkshopModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def workshop(request):
        # workshops = Workshop.objects.filter(status=1)
        # context = {'workshops':workshops}
        return render(request, template_name='research/workshop.html', context={})

    def add_workshop(request):

        if request.method == 'POST' and request.FILES['logo']:

            partner_form = WorkshopForm(request.POST,request.FILES)

            if partner_form.is_valid():
                partner_name  = request.POST['workshop_name']
                website_url = request.POST['website_url']
                logo = request.FILES['logo']
                status = 1
                new_partner = Partner(partner_name=partner_name, website_url=website_url, logo=logo, status=status)

                get_objects = Partner.objects.filter(partner_name=partner_name, status=1)
                if get_objects:
                    messages.success(request, "Workshop already exist." )
                    workshop_form = WorkshopForm()
                    return render(request, template_name='research/add_workshop.html', context={'workshop_form':workshop_form})
                else:
                    new_partner.save()
                    workshops = Workshop.objects.filter(status=1)
                    context = {'workshops':workshops}
                    messages.success(request, "Workshop successful added." )
                    return render(request,'research/workshops.html', context=context)

            else:
                print(partner_form.errors.as_data())


        partner_form = PartnerForm()
        return render(request, template_name='research/add_workshop.html', context={'partner_form':partner_form})
    
    def edit_workshop(request,id):
        workshop = Workshop.objects.get(id=id)
        workshop_form = WorkshopForm()
        context = {'workshop':workshop, 'workshop_form':workshop_form}
        return render(request, template_name='research/edit_workshop.html', context=context)

    def deactivate_workshop(request,id):
        workshop = Workshop.objects.get(id=id)
        workshop.status = 0
        workshop.save()
        return redirect('workshop:workshops')

    def delete_workshop(request,id):
        workshop = Workshop.objects.filter(id=id)
        if workshop:
            workshop.delete()
            messages.success(request, "workshop deleted." )
            return redirect('workshop:workshops')
        messages.success(request, "Workshop doesn't exist." )
        return redirect('workshop:workshops')
    

    def workshops(request):
        workshops = Workshop.objects.all()
        context = {'workshops':workshops}
        return render(request, template_name='research/workshops.html', context=context)