from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Enterpriseprofile

class EnterpriseprofileList(ListView):
	model = Enterpriseprofile

class EnterpriseprofileDetail(DetailView):
	model = Enterpriseprofile
