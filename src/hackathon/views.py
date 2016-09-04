from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserFieldsForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def hackathon_home(request):
	if (request.user.is_authenticated()):
		print request.user
	else:
		print "no hay usuario autenticado"
	context = {}
	return render(request, "hackathon-home.html", context)


def hackathon_sign_up(request):
	form = UserFieldsForm(request.POST or None)
	if form.is_valid():
		# print form
		instance = form.save(commit = False)
		username = instance.username
		password = instance.password
		email = instance.email

		user_exist = User.objects.filter(username = username)
		if (len(user_exist) > 0):
			messages.error(request, 'Este usuario ya existe')
		else: 
			flag = False
			if (email != ""):
				email_exist = User.objects.filter(email = email)
				if (len(email_exist) > 0):
					messages.error(request, 'Este correo ya esta registrado')
				else:
					flag = True
			else:
				flag = True
			if (flag):
				user = User.objects.create_user(username)
				user.set_password(password)
				if (email != ""):
					user.email = email
				user.save()
				new_user = authenticate(username = username, password = password)
				login(request, new_user)
				return redirect("/ambientapp/home")
	else: 
		form = UserFieldsForm()
	context = {
		"form": form
	}

	return render(request, "hackathon-sign-up.html", context)

def hackathon_log_in(request):
	context = {}
	if request.method == 'POST':
		username = request.POST['usuario']
		password = request.POST['password']
		user_by_username = authenticate(username = username, password = password)
		user_by_email = authenticate(email = username, password = password)
		if user_by_username is not None:
			messages.success(request, "Bienvenido "+username)
			login(request, user_by_username)
			return redirect("/ambientapp/home")
		else:
			if user_by_email is not None:
				query_set = User.objects.filter(email = username)
				usuario = query_set[0]['username']
				messages.success(request, "Bienvenido "+usuario)	
			else:
				messages.error(request, "Este usuario no existe")

	return render(request, "hackathon-log-in.html", context)

def hackathon_log_out(request):
	context = {}
	logout(request)	
	return redirect("/ambientapp/home")


def hackathon_hdc(request):
	context = {}
	if (request.method == "POST"):
		return redirect("/ambientapp/resultado")
	return render(request, "hackathonHuellaCarbono.html", context)

def hackathon_after_hdc(request):
	context = {
		"mundos": 1.2
	} 
	return render(request, "hackathonResultados.html", context)

def hackathon_high_scores(request):
	context = {}

	return render(request, "hackathon-high-scores.html", context)