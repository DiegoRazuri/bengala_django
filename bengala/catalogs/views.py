from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView
from .models import Catalog
from enterpriseprofiles.models import Enterpriseprofile

class CatalogsList(ListView):
	#model = Catalog
	template_name = 'catalogs/catalog_list.html'

	def get_queryset(self):
		self.enterpriseprofile = get_object_or_404(Enterpriseprofile, id=self.args[0])
		return Catalog.objects.filter(enterprise = self.enterpriseprofile)