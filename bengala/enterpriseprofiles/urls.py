from django.conf.urls import url
from . import views
from . import forms

urlpatterns = [
    url(r'^$', views.EnterpriseprofileList.as_view(), name='listado'),
    url(r'^enterprise/new', views.new_enterprise, name='new_enterprise'),
    url(r'^enterprise/(?P<pk>[0-9]+)/$', views.enterpriseprofile_detail, name='enterprise_detail')
]