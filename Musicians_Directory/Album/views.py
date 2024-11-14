from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Album,Musician
from .forms import AlbumForm
# Create your views here.
@method_decorator(login_required,name='dispatch')
class CreateAlbum(CreateView):
    model=Album
    form_class=AlbumForm
    template_name='add_album.html'
    success_url=reverse_lazy("Homepage")
@method_decorator(login_required,name='dispatch')
class EditAlbum(UpdateView):
    model=Album
    form_class=AlbumForm
    template_name='add_album.html'
    success_url=reverse_lazy("Homepage")
    pk_url_kwarg='id'
@method_decorator(login_required,name='dispatch')
class DeleteAlbum(DeleteView):
    model=Album
    form_class=AlbumForm
    template_name='delete_album.html'
    success_url=reverse_lazy("Homepage")
    pk_url_kwarg='id'



