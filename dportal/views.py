from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DPortal, PatientData
from .serializers import DPortalModelSerializer,PatientDataModelSerializer
from .forms import DataForm, PatientDataForm
from django.contrib import messages
import pandas as pd
from django.contrib.auth.models import User
# Create your views here.

class DPortalAPIView(APIView):

    def get(self, request):
        team = DPortal.objects.all()
        serializer = DPortalModelSerializer(team, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DPortalModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def data_list(request):
        data = DPortal.objects.all()
        context = {'data':data}
        return render(request, template_name='tools/data_list.html', context=context)

    def dportal(request):
        data = DPortal.objects.filter(publish=1, status=1)
        general_count = len(DPortal.objects.filter(thematic_area=0))
        health_count = len(DPortal.objects.filter(thematic_area=1))
        agriculture_count = len(DPortal.objects.filter(thematic_area=2))
        infra_count = len(DPortal.objects.filter(thematic_area=3))
        digital_count = len(DPortal.objects.filter(thematic_area=4))
        context = {"data": data,'general_count':general_count,'health_count':health_count,
                   'agriculture_count':agriculture_count, 'infra_count':infra_count,'digital_count':digital_count}
        return render(request, template_name='tools/data-portal.html', context=context)

    def add_data(request):

        if request.method == 'POST' and request.FILES['file']:

            news_form = DataForm(request.POST,request.FILES)

            if news_form.is_valid():
                name  = request.POST['name']
                description = request.POST['description']
                body = request.POST['body']
                file = request.FILES['file']
                thematic_area= request.POST['thematic_area']
                status = 1
                slug = name.replace(' ','-').lower()
                new_data = DPortal(name=name, description=description, body=body, file=file,thematic_area=thematic_area, status=status,publisher_id=request.session['user_id'], slug=slug)
                get_objects = DPortal.objects.filter(name=name, status=1)
                if get_objects:
                    messages.success(request, "Data already exist." )
                    data_form = DataForm()
                    return render(request, template_name='tools/add_data.html', context={'data_form':data_form})
                else:
                    new_data.save()
                    messages.success(request, "Data successful added." )
                    return redirect('dportal:data-list')
            else:
                print(data_form.errors.as_data())
                
        data_form = DataForm()
        return render(request, template_name='tools/add_data.html', context={'data_form':data_form})


    def review_data(request,id):
        data = DPortal.objects.get(id=id)
        data_file = None
        # if str(data.file).endswith(".xlsx"):
        #     data_file = pd.read_excel(data.file)
        # if str(data.file).endswith(".csv"):
        #     data_file = pd.read_excel(data.file)
        context = {'data':data}
        return render(request, template_name='tools/review_data.html', context=context)
    
    def read_data(request,slug):
        data = DPortal.objects.get(slug=slug)
        data_file = None
        # if str(data.file).endswith(".xlsx"):
        #     data_file = pd.read_excel(data.file)
        # if str(data.file).endswith(".csv"):
        #     data_file = pd.read_excel(data.file)
        #ata_file = data_file.head(5).to_html()
        publisher = User.objects.get(id=data.publisher_id)
        publisher_posts = DPortal.objects.filter(publisher_id=data.publisher_id).exclude(slug=slug)
        context = {'data':data, 'publisher_posts':publisher_posts,'publisher':publisher, 'publisher_posts':publisher_posts[:3]}
        return render(request, template_name='tools/data_single.html', context=context)
    
    def view_data(request,id):
        data = DPortal.objects.get(id=id)
        data_file = None
        # if str(data.file).endswith(".xlsx"):
        #     data_file = pd.read_excel(data.file)
        # if str(data.file).endswith(".csv"):
        #     data_file = pd.read_excel(data.file)
        context = {'data':data}
        return render(request, template_name='tools/view_data.html', context=context)
    
    def publish_data(request,id):
            data = DPortal.objects.get(id=id)
            data.publish = 1
            data.save()
            return redirect('dportal:data-list')
            
    
    def delete_data(request,id):
        data = DPortal.objects.filter(id=id)
        if data:
            data.delete()
            messages.success(request, "Data deleted." )
            return redirect('dportal:data-list')
        messages.success(request, "Data doesn't exist." )
        return redirect('dportal:dportal-list')


class PatientDataAPIView(APIView):

    def get(self, request):
        patient_data = PatientData.objects.all()
        serializer = PatientDataModelSerializer(patient_data, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PatientDataModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def patient_data_list(request):
        data = PatientData.objects.filter(user_id=request.session['user_id'])
        context = {'data':data}
        return render(request, template_name='tools/patient_data_list.html', context=context)

    def add_patient_data(request):

        if request.method == 'POST':

            form = PatientDataForm(request.POST,request.FILES)# Bind the form data to the Data form

            if form.is_valid():
                # Extract data from the form
                patient_id = form.cleaned_data['patient_id']
                age = form.cleaned_data['age']
                country = form.cleaned_data['country']
                district = form.cleaned_data['district']
                region = form.cleaned_data['region']
                facility = form.cleaned_data['facility']
                main_complaint = form.cleaned_data['main_complaint']
                history_of_present_illness = form.cleaned_data['history_of_present_illness']
                review_of_other_systems = form.cleaned_data['review_of_other_systems']
                past_medical_history = form.cleaned_data['past_medical_history']
                gynaecological_history = form.cleaned_data['gynaecological_history']
                family_social_history = form.cleaned_data['family_social_history']
                dietary_history = form.cleaned_data['dietary_history']
                general_examination = form.cleaned_data['general_examination']
                local_examination = form.cleaned_data['local_examination']
                systemic_examination = form.cleaned_data['systemic_examination']
                provisional_diagnosis = form.cleaned_data['provisional_diagnosis']
                differential_diagnosis = form.cleaned_data['differential_diagnosis']
                final_diagnosis = form.cleaned_data['final_diagnosis']
                radiological = form.cleaned_data['radiological']
                laboratory = form.cleaned_data['laboratory']
                doctors_remarks = form.cleaned_data['doctors_remarks']
                medicines = form.cleaned_data['medicines']
                treatment_regime = form.cleaned_data['treatment_regime']
                recommendation = form.cleaned_data['recommendation']
                # Create and save a new PatientData object
                patient_data = PatientData(
                    patient_id=patient_id,
                    age=age,
                    country=country,
                    district=district,
                    region=region,
                    facility=facility,
                    main_complaint=main_complaint,
                    history_of_present_illness=history_of_present_illness,
                    review_of_other_systems=review_of_other_systems,
                    past_medical_history=past_medical_history,
                    gynaecological_history=gynaecological_history,
                    family_social_history=family_social_history,
                    dietary_history=dietary_history,
                    general_examination=general_examination,
                    local_examination=local_examination,
                    systemic_examination=systemic_examination,
                    provisional_diagnosis=provisional_diagnosis,
                    differential_diagnosis=differential_diagnosis,
                    final_diagnosis=final_diagnosis,
                    radiological=radiological,
                    laboratory=laboratory,
                    doctors_remarks=doctors_remarks,
                    medicines=medicines,
                    treatment_regime=treatment_regime,
                    recommendation=recommendation,
                    user_id = request.session['user_id']
                )

                get_objects = PatientData.objects.filter(patient_id=patient_id)
                if get_objects:
                    messages.success(request, "Data already exist." )
                    data_form = PatientDataForm()
                    return render(request, template_name='tools/patient_data_collection.html', context={'form':data_form})
                else:
                    patient_data.save()
                    messages.success(request, "Data successful added." )
                    return redirect('dportal:patient-data-list')
            else:
                print(data_form.errors.as_data())
                
        data_form = PatientDataForm()
        return render(request, template_name='tools/patient_data_collection.html', context={'form':data_form})


    def review_patient_data(request,id):
        data = DPortal.objects.get(id=id)
        data_file = None
        # if str(data.file).endswith(".xlsx"):
        #     data_file = pd.read_excel(data.file)
        # if str(data.file).endswith(".csv"):
        #     data_file = pd.read_excel(data.file)
        context = {'data':data}
        return render(request, template_name='tools/review_data.html', context=context)
            
    
    def delete_patient_data(request,id):
        data = DPortal.objects.filter(id=id)
        if data:
            data.delete()
            messages.success(request, "Data deleted." )
            return redirect('dportal:data-list')
        messages.success(request, "Data doesn't exist." )
        return redirect('dportal:dportal-list')