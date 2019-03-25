from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item, Category, Transaction


class HomePageView(LoginRequiredMixin, TemplateView):
	"""docstring for HomePageView"""
	template_name = 'pages/home.html'
	login_url = '/accounts/login/'

	def get_context_data(self, **kwargs):
	    context = super(HomePageView, self).get_context_data(**kwargs)
	    context['items'] = Item.objects.all()
	    context['transactions'] = Transaction.objects.all()
	    return context


class ItemCreateView(CreateView):
	model = Item
	fields = '__all__'
	success_url = '/'


class ItemUpdateView(UpdateView):
	model = Item
	fields = '__all__'
	success_url = '/'


class CategoryCreateView(CreateView):
	model = Category
	fields = '__all__'
	success_url = '/'
		