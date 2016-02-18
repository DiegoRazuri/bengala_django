from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Enterpriseprofile
#from django.views.generic.edit import CreateView
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .forms import EnterpriseprofileForm

class EnterpriseprofileList(ListView):
	model = Enterpriseprofile

class EnterpriseprofileDetail(DetailView):
	model = Enterpriseprofile
'''
class EnterpriseprofileCreate(CreateView):
	model = Enterpriseprofile
	
	def form_valid(self, form):
		self.object = form.save(commit=False)

		for enterprise in form.cleaned_data['relationship']:
			relationship = Client()
			relationship.client = self.object
			relationship.enterprise = enterprise
			relationship.save()
		return super(ModelFormMixin, self).form_valid(form)
'''
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