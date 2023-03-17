from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Call
from .serializers import CallModelSerializer
from django.contrib import messages
from .forms import CallForm
from django.contrib.auth.models import User
# Create your views here.

class CallAPIView(APIView):

    def get(self, request):
        calls = Call.objects.all()
        serializer = CallModelSerializer(calls, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CallModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def call_list(request):
        calls = Call.objects.all()
        context = {'calls':calls}
        return render(request, template_name='updates/call_list.html', context=context)

    def call(request):
        calls = Call.objects.filter(publish=1, status=1)
        context = {"calls": calls}
        return render(request, template_name='updates/call.html', context=context)

    def add_call(request):

        if request.method == 'POST' and request.FILES['thumbnail']:

            call_form = CallForm(request.POST,request.FILES)

            if call_form.is_valid():
                title  = request.POST['title']
                description = request.POST['description']
                body = request.POST['body']
                thumbnail = request.FILES['thumbnail']
                header_image = request.FILES['header_image']
                file= request.FILES['file']
                thematic_area= request.POST['thematic_area']
                status = 1
                slug = title.replace(' ','-').lower()
                new_call = Call(title=title, description=description, body=body, thumbnail=thumbnail,file=file,thematic_area=thematic_area, header_image=header_image, status=status,publisher_id=request.session['user_id'], slug=slug)
                get_objects = Call.objects.filter(title=title, status=1)
                if get_objects:
                    messages.success(request, "call already exist." )
                    call_form = CallForm()
                    return render(request, template_name='updates/add_call.html', context={'call_form':call_form})
                else:
                    new_call.save()
                    messages.success(request, "call successful added." )
                    return redirect('call:call-list')
            else:
                print(call_form.errors.as_data())
                
        call_form = CallForm()
        return render(request, template_name='updates/add_call.html', context={'call_form':call_form})


    def review_call(request,id):
        call = Call.objects.get(id=id)
        context = {'call':call}
        return render(request, template_name='updates/review_call.html', context=context)
    
    def read_call(request,slug):
        call = Call.objects.get(slug=slug)
        publisher = User.objects.get(id=call.publisher_id)
        publisher_posts = Call.objects.filter(publisher_id=call.publisher_id).exclude(slug=slug)
        context = {'call':call, 'publisher_posts':publisher_posts,'publisher':publisher, 'publisher_posts':publisher_posts[:3]}
        return render(request, template_name='updates/call_single.html', context=context)
    
    def view_call(request,id):
        call = call.objects.get(id=id)
        context = {'call':call}
        return render(request, template_name='updates/view_call.html', context=context)
    
    def publish_call(request,id):
            call = Call.objects.get(id=id)
            call.publish = 1
            call.save()
            return redirect('call:call-list')
            
    
    def delete_call(request,id):
        call = Call.objects.filter(id=id)
        if call:
            call.delete()
            messages.success(request, "call deleted." )
            return redirect('call:call-list')
        messages.success(request, "call doesn't exist." )
        return redirect('call:call-list')