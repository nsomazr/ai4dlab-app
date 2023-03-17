from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UDOMAI,AI4D,GirlsinAI
from .serializers import UDOMAIModelSerializer
from .forms import UDOMAIForm,AI4DForm, GirlsinAIForm
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
    
    def register_ai4d_member(request):

        if request.method == 'POST':

            ai4d_form = AI4DForm(request.POST)

            if ai4d_form.is_valid():
                first_name  = request.POST['first_name']
                last_name = request.POST['last_name']
                country = request.POST['country']
                affiliation = request.POST['affiliation']
                field= request.POST['field']
                phone = request.POST['phone']
                email = request.POST['email']
                status = 1
                new_ai4d_member = AI4D(first_name=first_name, last_name=last_name,country=country,affiliation=affiliation, field=field,phone=phone,email=email, status=status)

                get_objects = AI4D.objects.filter(email=email,status=1)
                if get_objects:
                    messages.success(request, "Member already exist." )
                    ai4d_form = UDOMAIForm()
                    return render(request, template_name='community/register_ai4d.html', context={'ai4d_form':ai4d_form})
                else:
                    new_ai4d_member.save()
                    ai4d_members = AI4D.objects.filter(status=1)
                    context = {'ai4d_members':ai4d_members}
                    messages.success(request, "You have successful registered." )
                    return render(request,'community/ai4d_community.html', context=context)

            else:
                print(ai4d_form.errors.as_data())


        ai4d_form = AI4DForm()
        return render(request, template_name='community/register_ai4d.html', context={'ai4d_form':ai4d_form})

    def ai4d_member(request,id):
        ai4d_member = AI4D.objects.get(id=id)
        context = {'ai4d_member':ai4d_member}
        return render(request, template_name='community/ai4d_member.html', context=context)

    def deactivate_ai4d_member(request,id):
        ai4d_member = AI4D.objects.get(id=id)
        ai4d_member.status = 0
        ai4d_member.save()
        return redirect('community:ai4d-members')

    def delete_ai4d_member(request,id):
        ai4d_member = AI4D.objects.filter(id=id)
        if ai4d_member:
            ai4d_member.delete()
            messages.success(request, "Member deleted." )
            return redirect('community:ai4d-members')
        messages.success(request, "Member doesn't exist." )
        return redirect('community:ai4d-members')

    def ai4d_members(request):
        ai4d_members = AI4D.objects.all()
        context = {'ai4d_members':ai4d_members}
        
        return render(request, template_name='community/ai4d_members.html', context=context)

    
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
    
    def register_girlsinai_member(request):

        if request.method == 'POST':

            girlsinai_form = GirlsinAIForm(request.POST)

            if girlsinai_form.is_valid():
                first_name  = request.POST['first_name']
                last_name = request.POST['last_name']
                country = request.POST['country']
                affiliation = request.POST['affiliation']
                field= request.POST['field']
                phone = request.POST['phone']
                email = request.POST['email']
                status = 1
                new_girlsinai_member = GirlsinAI(first_name=first_name, last_name=last_name,country=country,affiliation=affiliation, field=field,phone=phone,email=email, status=status)

                get_objects = GirlsinAI.objects.filter(email=email,status=1)
                if get_objects:
                    messages.success(request, "Member already exist." )
                    girlsinai_form = GirlsinAIForm()
                    return render(request, template_name='community/register_girlsinai.html', context={'girlsinai_form':girlsinai_form})
                else:
                    new_girlsinai_member.save()
                    girlsinai_members = GirlsinAI.objects.filter(status=1)
                    context = {'ai4d_members':girlsinai_members}
                    messages.success(request, "You have successful registered." )
                    return render(request,'community/girlsinai_community.html', context=context)

            else:
                print(girlsinai_form.errors.as_data())


        girlsinai_form = GirlsinAIForm()
        return render(request, template_name='community/register_girlsinai.html', context={'girlsinai_form':girlsinai_form})

    def girlsinai_member(request,id):
        girlsinai_member = GirlsinAI.objects.get(id=id)
        context = {'girlsinai_member':girlsinai_member}
        return render(request, template_name='community/ai4d_member.html', context=context)

    def deactivate_girlsinai_member(request,id):
        girlsinai_member = GirlsinAI.objects.get(id=id)
        girlsinai_member.status = 0
        girlsinai_member.save()
        return redirect('community:girlsinai-members')

    def delete_girlsinai_member(request,id):
        girlsinai_member = GirlsinAI.objects.filter(id=id)
        if girlsinai_member:
            girlsinai_member.delete()
            messages.success(request, "Member deleted." )
            return redirect('community:girlsinai-members')
        messages.success(request, "Member doesn't exist." )
        return redirect('community:girlsinai-members')

    def girlsinai_members(request):
        girlsinai_members = GirlsinAI.objects.all()
        context = {'girlsinai_members':girlsinai_members}
        
        return render(request, template_name='community/girlsinai_members.html', context=context)

    # End Girls in AI

   
