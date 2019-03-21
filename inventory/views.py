from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(LoginRequiredMixin, TemplateView):
	"""docstring for HomePageView"""
	template_name = 'pages/home.html'
	login_url = '/accounts/login/'
		