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

    def aaiac_23(request):
        return render(request, template_name='conference/aaiac2023/index.html', context={})
    
    def aaiac_23_contacts(request):
        return render(request, template_name='conference/aaiac2023/contacts.html', context={})

    def aaiac_23_organizers(request):
        return render(request, template_name='conference/aaiac2023/organizers.html', context={})
    
    def aaiac_23_call_for_paper(request):
        return render(request, template_name='conference/aaiac2023/call_for_paper.html', context={})

    def aaiac_23_speaker_malanga(request):
        return render(request, template_name='conference/aaiac2023/malanga.html', context={})

    def aaiac_23_speaker_andre(request):
        return render(request, template_name='conference/aaiac2023/andre.html', context={})

    def aaiac_23_speaker_chao(request):
        return render(request, template_name='conference/aaiac2023/chao.html', context={})

    def aaiac_23_speaker_denhere(request):
        return render(request, template_name='conference/aaiac2023/denhere.html', context={})

    def aaiac_23_speaker_deo(request):
        return render(request, template_name='conference/aaiac2023/deo.html', context={})
    
    def aaiac_23_speaker_dina(request):
        return render(request, template_name='conference/aaiac2023/dina.html', context={})

    def aaiac_23_speaker_essa(request):
        return render(request, template_name='conference/aaiac2023/essa.html', context={})

    def aaiac_23_speaker_gomez(request):
        return render(request, template_name='conference/aaiac2023/gomez.html', context={})

    def aaiac_23_speaker_juma(request):
        return render(request, template_name='conference/aaiac2023/juma.html', context={})

    def aaiac_23_speaker_jumanne(request):
        return render(request, template_name='conference/aaiac2023/jumanne.html', context={})

    def aaiac_23_speaker_kadeghe(request):
        return render(request, template_name='conference/aaiac2023/kadeghe.html', context={})
    
    def aaiac_23_speaker_lee(request):
        return render(request, template_name='conference/aaiac2023/leo.html', context={})

    def aaiac_23_speaker_linder(request):
        return render(request, template_name='conference/aaiac2023/linder.html', context={})

    def aaiac_23_speaker_mahadia(request):
        return render(request, template_name='conference/aaiac2023/mahadia.html', context={})

    def aaiac_23_speaker_mboni(request):
        return render(request, template_name='conference/aaiac2023/mboni.html', context={})

    def aaiac_23_speaker_mpho(request):
        return render(request, template_name='conference/aaiac2023/mpho.html', context={})

    def aaiac_23_speaker_msanjila(request):
        return render(request, template_name='conference/aaiac2023/msanjila.html', context={})

    def aaiac_23_speaker_mussa(request):
        return render(request, template_name='conference/aaiac2023/mussa.html', context={})

    def aaiac_23_speaker_sokhela(request):
        return render(request, template_name='conference/aaiac2023/sokhela.html', context={})
    
    def aaiac_23_speaker_thomas(request):
        return render(request, template_name='conference/aaiac2023/thomas.html', context={})