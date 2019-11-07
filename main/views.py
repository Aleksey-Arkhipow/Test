from django.shortcuts import render
from django.contrib.auth. views import LoginView

class BBLoginView(LoginView):
	template_name = 'main/login.html'
	