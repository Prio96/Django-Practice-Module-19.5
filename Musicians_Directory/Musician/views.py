from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,DeleteView
from django.forms import BaseModelForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
# Create your views here.
 