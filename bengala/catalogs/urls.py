from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^enterprise/([\w-]+)/catalog/$', views.CatalogsList.as_view(), name='listado_catalogs'),
    #url(r'^enterprise/new', views.new_enterprise, name='new_enterprise'),
    #url(r'^enterprise/(?P<pk>[0-9]+)/$', views.EnterpriseprofileDetail.as_view(), name='enterprise_detail')
]