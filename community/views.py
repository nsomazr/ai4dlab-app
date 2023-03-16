from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UDOMAI
from .serializers import UDOMAIModelSerializer
from .forms import UDOMAIForm
from django.contrib import messages
# Create your views here.

class CommunityAPIView(APIView):

    def get(self, request):
        udomai_community = UDOMAI.objects.all()
        serializer = UDOMAIModelSerializer(udomai_community, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UDOMAIModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)


    def ai4d_community(request):

        return render(request, template_name='community/ai4d_community.html', context={})
    
    
    # End AI4D
    
    def udomai_community(request):

        return render(request, template_name='community/udomai_community.html', context={})

    def register_udomai_member(request):

        if request.method == 'POST':

            udomai_form = UDOMAIForm(request.POST)

            if udomai_form.is_valid():
                first_name  = request.POST['first_name']
                last_name = request.POST['last_name']
                college = request.POST['college']
                programme = request.POST['programme']
                yos= request.POST['yos']
                phone = request.POST['phone']
                email = request.POST['email']
                status = 1
                new_udomai_member = UDOMAI(first_name=first_name, last_name=last_name,college=college,programme=programme,yos=yos,phone=phone,email=email, status=status)

                get_objects = UDOMAI.objects.filter(email=email,status=1)
                if get_objects:
                    messages.success(request, "Member already exist." )
                    udomai_form = UDOMAIForm()
                    return render(request, template_name='community/register_udomai.html', context={'udomai_form':udomai_form})
                else:
                    new_udomai_member.save()
                    udomai_members = UDOMAI.objects.filter(status=1)
                    context = {'udomai_members':udomai_members}
                    messages.success(request, "You have successful registered." )
                    return render(request,'community/udomai_community.html', context=context)

            else:
                print(udomai_form.errors.as_data())


        udomai_form = UDOMAIForm()
        return render(request, template_name='community/register_udomai.html', context={'udomai_form':udomai_form})

    def udomai_member(request,id):
        udomai_member = UDOMAI.objects.get(id=id)
        context = {'udomai_member':udomai_member}
        return render(request, template_name='community/udomai_member.html', context=context)

    def deactivate_udomai_member(request,id):
        udomai_member = UDOMAI.objects.get(id=id)
        udomai_member.status = 0
        udomai_member.save()
        return redirect('community:udomai-members')

    def delete_udomai_member(request,id):
        udomai_member = UDOMAI.objects.filter(id=id)
        if udomai_member:
            udomai_member.delete()
            messages.success(request, "Member deleted." )
            return redirect('community:udomai-members')
        messages.success(request, "Member doesn't exist." )
        return redirect('community:udomai-members')

    def udomai_members(request):
        udomai_members = UDOMAI.objects.all()
        context = {'udomai_members':udomai_members}
        
        return render(request, template_name='community/udomai_members.html', context=context)

    # End UDOMAI

    def girlsinai_community(request):

        return render(request, template_name='community/girlsinai_community.html', context={})

    def ai4d_members(request):

        return render(request, template_name='community/ai4d_members.html', context={})

    def girslinai_members(request):

        return render(request, template_name='community/girlsinai_members.html', context={})