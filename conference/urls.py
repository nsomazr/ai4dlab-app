from django.urls import path
from .views import ConferenceAPIView
from django.conf import settings
from django.conf.urls.static import static
app_name = "conference"  

urlpatterns = [path('', ConferenceAPIView.aaiac_23, name="aaiac-23"),
               path('AAIAC/2023/contacts/', ConferenceAPIView.aaiac_23_contacts, name="aaiac-23-contacts"),
               path('AAIAC/2023/organizers/', ConferenceAPIView.aaiac_23_organizers, name="aaiac-23-organizers"),
               path('AAIAC/2023/call-for-paper/', ConferenceAPIView.aaiac_23_call_for_paper, name="aaiac-23-call-for-paper"),
               path('AAIAC/2023/speaker/malanga', ConferenceAPIView.aaiac_23_speaker_malanga, name="speaker-malanga"),
               path('AAIAC/2023/speaker/andre', ConferenceAPIView.aaiac_23_speaker_andre, name="speaker-andre"),
               path('AAIAC/2023/speaker/chao', ConferenceAPIView.aaiac_23_speaker_chao, name="speaker-chao"),
               path('AAIAC/2023/speaker/denhere', ConferenceAPIView.aaiac_23_speaker_denhere, name="speaker-denhere"), 
               path('AAIAC/2023/speaker/deo', ConferenceAPIView.aaiac_23_speaker_deo, name="speaker-deo"),
               path('AAIAC/2023/speaker/dina', ConferenceAPIView.aaiac_23_speaker_dina, name="speaker-dina"),
               path('AAIAC/2023/speaker/essa', ConferenceAPIView.aaiac_23_speaker_essa, name="speaker-essa"),
               path('AAIAC/2023/speaker/gomez', ConferenceAPIView.aaiac_23_speaker_gomez, name="speaker-gomez"),
               path('AAIAC/2023/speaker/juma', ConferenceAPIView.aaiac_23_speaker_juma, name="speaker-juma"),  
               path('AAIAC/2023/speaker/jumanne', ConferenceAPIView.aaiac_23_speaker_jumanne, name="speaker-jumanne"), 
               path('AAIAC/2023/speaker/kadeghe', ConferenceAPIView.aaiac_23_speaker_kadeghe, name="speaker-kadeghe"),
               path('AAIAC/2023/speaker/lee', ConferenceAPIView.aaiac_23_speaker_lee, name="speaker-lee"),
               path('AAIAC/2023/speaker/linder', ConferenceAPIView.aaiac_23_speaker_linder, name="speaker-linder"),
               path('AAIAC/2023/speaker/mahadia', ConferenceAPIView.aaiac_23_speaker_mahadia, name="speaker-mahadia"),
               path('AAIAC/2023/speaker/mboni', ConferenceAPIView.aaiac_23_speaker_mboni, name="speaker-mboni"),
               path('AAIAC/2023/speaker/mpho', ConferenceAPIView.aaiac_23_speaker_mpho, name="speaker-mpho"),
               path('AAIAC/2023/speaker/msanjila', ConferenceAPIView.aaiac_23_speaker_msanjila, name="speaker-msanjila"),
               path('AAIAC/2023/speaker/mussa', ConferenceAPIView.aaiac_23_speaker_mussa, name="speaker-mussa"),
               path('AAIAC/2023/speaker/sokhela', ConferenceAPIView.aaiac_23_speaker_sokhela, name="speaker-sokhela"),
               path('AAIAC/2023/speaker/thomas', ConferenceAPIView.aaiac_23_speaker_thomas, name="speaker-thomas"),
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)