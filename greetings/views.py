from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.contrib import messages
from django.urls import reverse

from .models import Names
from .forms import NameForm

class GreetingView(CreateView):
	model = Names
	form_class = NameForm
	template_name = 'greetings/greeting.html'
	success_url = '/'

	def form_valid(self, form):
		messages.success(self.request, f"Привіт, {form.cleaned_data['first_name']} {form.cleaned_data['last_name']}")
		return super().form_valid(form)

	def form_invalid(self, form):
		messages.error(self.request, f"Вже бачилися, {form.cleaned_data['first_name']}")
		return super().form_invalid(form)

	def get_success_url(self):
		return reverse('greeting')



class NamesListView(ListView):
	paginate_by = 10
	model = Names