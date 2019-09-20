from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^question/\d+/?$', views.test),
   # url(r'^$', None),
   # url(r'^login/?$', None),
   # url(r'^signup?$', None),
   # url(r'^ask/?$', None),
   # url(r'^popular/?$', None),
   # url(r'^new/?$', None),
]