from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Partner
from .serializers import PartnerModelSerializer
from django.contrib import messages
from .forms import PartnerForm
# Create your views here.

class PartnerAPIView(APIView):

    def get(self, request):
        Partner = Partner.objects.all()
        serializer = PartnerModelSerializer(Partner, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PartnerModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def partner(request):
        partners = Partner.objects.filter(status=1)
        context = {'partners':partners}
        return render(request, template_name='about/partner.html', context=context)

    def add_partner(request):

        if request.method == 'POST' and request.FILES['logo']:

            partner_form = PartnerForm(request.POST,request.FILES)

            if partner_form.is_valid():
                partner_name  = request.POST['partner_name']
                website_url = request.POST['website_url']
                logo = request.FILES['logo']
                status = 1
                new_partner = Partner(partner_name=partner_name, website_url=website_url, logo=logo, status=status)

                get_objects = Partner.objects.filter(partner_name=partner_name, status=1)
                if get_objects:
                    messages.success(request, "partner already exist." )
                    Partner_form = PartnerForm()
                    return render(request, template_name='about/add_partner.html', context={'partner_form':partner_form})
                else:
                    new_partner.save()
                    partners = Partner.objects.filter(status=1)
                    context = {'partners':partners}
                    messages.success(request, "partner successful added." )
                    return render(request,'about/partners.html', context=context)

            else:
                print(partner_form.errors.as_data())


        partner_form = PartnerForm()
        return render(request, template_name='about/add_partner.html', context={'partner_form':partner_form})
    
    def edit_partner(request,id):
        partner = Partner.objects.get(id=id)
        partner_form = PartnerForm()
        context = {'partner':partner, 'partner_form':partner_form}
        return render(request, template_name='about/edit_partner.html', context=context)

    def deactivate_partner(request,id):
        partner = Partner.objects.get(id=id)
        partner.status = 0
        partner.save()
        return redirect('partner:partners')

    def delete_partner(request,id):
        partner = Partner.objects.filter(id=id)
        if partner:
            partner.delete()
            messages.success(request, "partner deleted." )
            return redirect('partner:partners')
        messages.success(request, "partner doesn't exist." )
        return redirect('partner:partners')
    

    def partners(request):
        partners = Partner.objects.all()
        context = {'partners':partners}
        return render(request, template_name='about/partners.html', context=context)