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

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except Exception:
            messages.error(self.request,
                           f"Seen you, {form.cleaned_data['first_name']}")
            return super().form_invalid(form)
        finally:
            if not messages.get_messages(self.request):
                messages.success(self.request,
                                 f"Hi, {form.cleaned_data['first_name']} {form.cleaned_data['last_name']}")

    def get_success_url(self):
        return reverse('greeting')


class NamesListView(ListView):
    paginate_by = 10
    model = Names
