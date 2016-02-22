from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Enterpriseprofile
#from django.views.generic.edit import CreateView
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import EnterpriseprofileForm
from catalogs.models import Catalog

class EnterpriseprofileList(ListView):
	model = Enterpriseprofile


def enterpriseprofile_detail(request, pk):
	enterpriseprofile = get_object_or_404(Enterpriseprofile, pk=pk)
	providers = Enterpriseprofile.objects.filter(relations__client__id=pk)
	album = enterpriseprofile.catalog.all()
	pubs_award = enterpriseprofile.award.all()
	pubs_certification = enterpriseprofile.certification.all()
	clients = enterpriseprofile.relations.filter(status=1)
#	providers = enterpriseprofile.relations.filter(relations__to_enterprise__id=pk)
	template = loader.get_template('enterpriseprofiles/enterpriseprofile_detail.html')
	context = {
	    'enterpriseprofile': enterpriseprofile,
	    'album': album,
	    'pubs_award': pubs_award,
	    'pubs_certification': pubs_certification,
	    'clients': clients,
	    'providers': providers
	}

	return HttpResponse(template.render(context, request))



def new_enterprise(request):
    if request.method == 'POST':
        form = EnterpriseprofileForm(request.POST, request.FILES)
        if form.is_valid():
        	enterprise = form.save(commit=False)
        	enterprise.save()
#ACA LO DEBERIA REDIRECCIONAR A LA VISTA DEL PERFIL Q SE ACABA DE CREAR
        	return HttpResponseRedirect('/')
    else:
    	form = EnterpriseprofileForm()
	
	template = loader.get_template('enterpriseprofiles/new_enterpriseprofile_form.html')
	context = {
	    'form': form
	}
	return HttpResponse(template.render(context, request))
'''
	consulta a la base de datos desde el shell 
	
	Enterpriseprofile.objects.filter(relations__client__id=1)
'''