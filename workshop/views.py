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
        workshops = Workshop.objects.filter(status=1, publish=1)
        context = {'workshops':workshops}
        return render(request, template_name='event/workshop.html', context=context)

    def add_workshop(request):

        if request.method == 'POST':

            workshop_form = WorkshopForm(request.POST)

            if workshop_form.is_valid():
                workshop_name  = request.POST['workshop_name']
                workshop_url = request.POST['workshop_url']
                description = request.POST['description']
                status = 1
                new_workshop = Workshop(workshop_name=workshop_name, workshop_url=workshop_url, description=description,publisher_id=request.session['user_id'], status=status)

                get_objects = Workshop.objects.filter(workshop_name=workshop_name, status=1)
                if get_objects:
                    messages.success(request, "Workshop already exist.")
                    workshop_form = WorkshopForm()
                    return render(request, template_name='event/add_workshop.html', context={'workshop_form':workshop_form})
                else:
                    new_workshop.save()
                    workshops = Workshop.objects.filter(status=1)
                    context = {'workshops':workshops}
                    messages.success(request, "Workshop successful added." )
                    return render(request,'event/workshop_list.html', context=context)

            else:
                print(workshop_form.errors.as_data())


        workshop_form = WorkshopForm()
        return render(request, template_name='event/add_workshop.html', context={'workshop_form':workshop_form})
    
    def edit_workshop(request,id):
        workshop = Workshop.objects.get(id=id)
        workshop_form = WorkshopForm()
        context = {'workshop':workshop, 'workshop_form':workshop_form}
        return render(request, template_name='event/edit_workshop.html', context=context)

    def deactivate_workshop(request,id):
        workshop = Workshop.objects.get(id=id)
        workshop.status = 0
        workshop.save()
        return redirect('workshop:workshop-list')

    def delete_workshop(request,id):
        workshop = Workshop.objects.filter(id=id)
        if workshop:
            workshop.delete()
            messages.success(request, "workshop deleted." )
            return redirect('workshop:workshop-list')
        messages.success(request, "Workshop doesn't exist." )
        return redirect('workshop:workshop-list')
    
    def review_workshop(request,id):
        workshop = Workshop.objects.get(id=id)
        context = {'workshop':workshop}
        return render(request, template_name='event/review_workshop.html', context=context)

    
    def view_workshop(request,id):
        workshop = Workshop.objects.get(id=id)
        context = {'workshop':workshop}
        return render(request, template_name='event/view_workshop.html', context=context)
    
    def publish_workshop(request,id):
            workshop = Workshop.objects.get(id=id)
            workshop.publish = 1
            workshop.save()
            return redirect('workshop:workshop-list')

    def workshop_list(request):
        workshops = Workshop.objects.all()
        context = {'workshops':workshops}
        return render(request, template_name='event/workshop_list.html', context=context)