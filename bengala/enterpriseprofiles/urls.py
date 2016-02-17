from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.EnterpriseprofileList.as_view(), name='listado'),
    url(r'^enterprise/(?P<pk>[0-9]+)/$', views.EnterpriseprofileDetail.as_view(), name='enterprise_detail')
]