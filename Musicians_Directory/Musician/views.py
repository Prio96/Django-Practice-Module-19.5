from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Musician
from .forms import MusicianForm
# Create your views here.
@method_decorator(login_required,name='dispatch')
class CreateMusicianClassView(CreateView):
    model=Musician
    form_class=MusicianForm
    template_name='add_musician.html'
    success_url=reverse_lazy("Homepage")
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Add'
        return context
@method_decorator(login_required,name='dispatch')
class EditMusicianClassView(UpdateView):
    model=Musician
    form_class=MusicianForm
    template_name='add_musician.html'
    success_url=reverse_lazy("Homepage")
    pk_url_kwarg='id'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='Edit'
        return context




