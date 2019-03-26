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


class ItemCreateView(LoginRequiredMixin, CreateView):
	model = Item
	fields = '__all__'
	success_url = '/'


class ItemUpdateView(LoginRequiredMixin, UpdateView):
	model = Item
	fields = '__all__'
	success_url = '/'


class CategoryCreateView(LoginRequiredMixin, CreateView):
	model = Category
	fields = '__all__'
	success_url = '/'


class TransactionCreateView(LoginRequiredMixin, CreateView):
	model = Transaction
	fields = ['quantity', 'Client']
	success_url = '/'

	def get_initial(self):
		return {'item': self.kwargs['item_pk']}

	def get_context_data(self, **kwargs):
	    context = super(TransactionCreateView, self).get_context_data(**kwargs)
	    context['item'] = Item.objects.get(id=self.kwargs['item_pk'])
	    return context

	def form_valid(self, form):
		item = Item.objects.get(id=self.kwargs['item_pk'])
		form.instance.item = item
		tran_type = self.request.POST.get('tran_type')

		if tran_type == 'in':
			item.quantity += int(self.request.POST.get('quantity'))
		else:
			if item.quantity >= int(self.request.POST.get('quantity')):
				item.quantity -= int(self.request.POST.get('quantity'))
				form.instance.quantity *= -1
			else:
				form.add_error('quantity', "Quantity is grather than item's quantity")
				return super(TransactionCreateView, self).form_invalid(form)
		item.save()

		return super(TransactionCreateView, self).form_valid(form)
		