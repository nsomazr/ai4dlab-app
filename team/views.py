from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Team
from .serializers import TeamModelSerializer
from django.contrib import messages
from .forms import TeamForm
# Create your views here.

class TeamAPIView(APIView):

    def get(self, request):
        team = Team.objects.all()
        serializer = TeamModelSerializer(team, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeamModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def team(request):
        members = Team.objects.filter(status=1)
        context = {'members':members}
        return render(request, template_name='about/our-team.html', context=context)

    def add_member(request):

        if request.method == 'POST' and request.FILES['photo']:

            team_form = TeamForm(request.POST,request.FILES)

            if team_form.is_valid():
                first_name  = request.POST['first_name']
                last_name = request.POST['last_name']
                title = request.POST['title']
                affiliation = request.POST['affiliation']
                bio = request.POST['bio']
                phone = request.POST['phone']
                email = request.POST['email']
                linkedin_url = request.POST['linkedin_url']
                twitter_url = request.POST['twitter_url']
                photo = request.FILES['photo']
                status = 1
                new_team_member = Team(first_name=first_name, last_name=last_name,title=title,affiliation=affiliation,
                                        bio=bio,phone=phone,email=email, status=status, linkedin_url=linkedin_url, twitter_url=twitter_url, photo=photo)

                get_objects = Team.objects.filter(email=email,status=1)
                if get_objects:
                    messages.success(request, "Member already exist." )
                    team_form = TeamForm()
                    return render(request, template_name='about/add_member.html', context={'team_form':team_form})
                else:
                    new_team_member.save()
                    members = Team.objects.filter(status=1)
                    context = {'members':members}
                    messages.success(request, "Member successful added." )
                    return render(request,'about/members.html', context=context)

            else:
                print(team_form.errors.as_data())


        team_form = TeamForm()
        return render(request, template_name='about/add_member.html', context={'team_form':team_form})

    def team_member(request,id):
        member = Team.objects.get(id=id)
        context = {'member':member}
        return render(request, template_name='about/team_member.html', context=context)

    def edit_member(request,id):
        member = Team.objects.get(id=id)
        team_form = TeamForm()
        context = {'member':member, 'team_form':team_form}
        return render(request, template_name='about/edit_member.html', context=context)

    def deactivate_member(request,id):
        member = Team.objects.get(id=id)
        member.status = 0
        member.save()
        return redirect('team:members')

    def delete_member(request,id):
        member = Team.objects.filter(id=id)
        if member:
            member.delete()
            members = Team.objects.all()
            context = {'members':members}
            messages.success(request, "Member deleted." )
            return redirect('team:members')
        members = Team.objects.all()
        context = {'members':members}
        messages.success(request, "Member doesn't exist." )
        return redirect('team:members')

    def members(request):
        members = Team.objects.all()
        context = {'members':members}
        return render(request, template_name='about/members.html', context=context)