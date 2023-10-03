from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserModelSerializer, MyTokenObtainPairSerializer
from django.contrib.auth.models import User
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm 
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMultiAlternatives
from django import template
from .forms import UserLoginForm, ResetPasswordForm
from .forms import StaffForm

class UsersAPIView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserModelSerializer(users, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


def register_request(request):
    if request.method == 'POST':
       register_form = NewUserForm(request.POST)
       if register_form.is_valid():
          user = register_form.save()
          username = register_form.cleaned_data.get('username')
          messages.success(request, "Registration successful." )
        #   login(request, user)
          login(request, user, backend='django.contrib.auth.backends.ModelBackend')
          return redirect("users:dashboard")
       else:
          messages.error(request,"Account creation failed")
          print(register_form.errors.as_data()) # here you print errors to terminal
          return redirect("users:register")

    register_form = NewUserForm()
    return render (request=request, template_name="users/register.html", context={"register_form":register_form})

def update_user(request,id):
		user= User.objects.get(id=id)
		update_form = NewUserForm(instance=user)# prepopulate the form with an existing band
		return render(request, 'users/update_user.html',{'update_form': update_form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			print("Get in")
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			print("Here")
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				print("Login")
				# if user.is_superuser or user.is_staff:
				# 	request.session['user_id'] = user.id
				# 	return redirect("users:dashboard")
				# else:
				# 	return redirect("home:home")
				request.session['user_id'] = user.id
				return redirect("users:dashboard")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	login_form = UserLoginForm()
	return render(request=request, template_name="users/login.html", context={"login_form":login_form})

def dashboard(request):

    return render(request, template_name = 'dashboards/admin.html', context={})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home:home")

#email sms single alternative

# def password_reset_request(request):
# 	if request.method == "POST":
# 		password_reset_form = PasswordResetForm(request.POST)
# 		if password_reset_form.is_valid():
# 			data = password_reset_form.cleaned_data['email']
# 			associated_users = User.objects.filter(Q(email=data))
# 			if associated_users.exists():
# 				for user in associated_users:
# 					subject = "Password Reset Requested"
# 					email_template_name = "main/password/password_reset_email.txt"
# 					c = {
# 					"email":user.email,
# 					'domain':'127.0.0.1:8000',
# 					'site_name': 'Website',
# 					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
# 					'token': default_token_generator.make_token(user),
# 					'protocol': 'http',
# 					}
# 					email = render_to_string(email_template_name, c)
# 					try:
# 						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
# 					except BadHeaderError:

# 						return HttpResponse('Invalid header found.')
						
# 					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
# 					return redirect ("main:homepage")
# 			messages.error(request, 'An invalid email has been entered.')
# 	password_reset_form = PasswordResetForm()
# 	return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form":password_reset_form})

# send email multi alternative
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = ResetPasswordForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data)|Q(username=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					plaintext = template.loader.get_template('users/password/password_reset_email.txt')
					htmltemp = template.loader.get_template('users/password/password_reset_email.html')
					c = { 
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					text_content = plaintext.render(c)
					html_content = htmltemp.render(c)
					try:
						msg = EmailMultiAlternatives(subject, text_content, 'Website nsoma.me>', [user.email], headers = {'Reply-To': 'ai@nsoma.me'})
						msg.attach_alternative(html_content, "text/html")
						msg.send()
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					messages.info(request, "Password reset instructions have been sent to the email address entered.")
					return redirect ("password_reset_done")
	password_reset_form = ResetPasswordForm()
	return render(request=request, template_name="users/password/password_reset.html", context={"password_reset_form":password_reset_form})


def add_staff(request):
    if request.method == 'POST':
       staff_form = StaffForm(request.POST)
       if staff_form.is_valid():
          user = staff_form.save()
          username = staff_form.cleaned_data.get('username')
          messages.success(request, "Registration successful." )
        #   login(request, user)
        #   login(request, user, backend='django.contrib.auth.backends.ModelBackend')
          return redirect("users:staffs")
       else:
          messages.error(request,"Account creation failed")
          print(staff_form.errors.as_data()) 
          return redirect("users:add-staff")

    staff_form = StaffForm()
    return render (request=request, template_name="users/add_staff.html", context={"staff_form":staff_form})

def staffs(request):
	staffs = User.objects.all()
	context = {'staffs':staffs}
	return render(request, template_name='users/staffs.html', context=context)
