from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import messages
from .models import Colab
from .serializers import ColabModelSerializer
from .forms import ColabForm
# Create your views here.

class ColabAPIView(APIView):

    def get(self, request):
        colabs = Colab.objects.all()
        serializer = ColabModelSerializer(colabs, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ColabModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def colab(request):
            colabs = Colab.objects.filter(status=1)
            context = {'colabs':colabs}
            return render(request, template_name='about/colab.html', context=context)

    def add_colab(request):

        if request.method == 'POST' and request.FILES['logo']:

            colab_form = ColabForm(request.POST,request.FILES)

            if colab_form.is_valid():
                colab_name  = request.POST['colab_name']
                website_url = request.POST['website_url']
                logo = request.FILES['logo']
                status = 1
                new_colab = Colab(colab_name=colab_name, website_url=website_url, logo=logo, status=status)

                get_objects = Colab.objects.filter(colab_name=colab_name, status=1)
                if get_objects:
                    messages.success(request, "Collaborator already exist." )
                    colab_form = ColabForm()
                    return render(request, template_name='about/add_colab.html', context={'colab_form':colab_form})
                else:
                    new_colab.save()
                    colabs = Colab.objects.filter(status=1)
                    context = {'colabs':colabs}
                    messages.success(request, "Collaborator successful added." )
                    return render(request,'about/colabs.html', context=context)

            else:
                print(colab_form.errors.as_data())


        colab_form = ColabForm()
        return render(request, template_name='about/add_colab.html', context={'colab_form':colab_form})
    
    def edit_colab(request,id):
        colab = Colab.objects.get(id=id)
        colab_form = ColabForm()
        context = {'colab':colab, 'colab_form':colab_form}
        return render(request, template_name='about/edit_colab.html', context=context)

    def deactivate_colab(request,id):
        colab = Colab.objects.get(id=id)
        colab.status = 0
        colab.save()
        return redirect('colab:colabs')

    def delete_colab(request,id):
        colab = Colab.objects.filter(id=id)
        if colab:
            colab.delete()
            messages.success(request, "Collaborator deleted." )
            return redirect('colab:colabs')
        messages.success(request, "Collaborator doesn't exist." )
        return redirect('colab:colabs')
    

    def colabs(request):
        colabs = Colab.objects.all()
        context = {'colabs':colabs}
        return render(request, template_name='about/colabs.html', context=context)