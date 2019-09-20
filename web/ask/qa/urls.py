from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^question/\d+/?$', views.test),
        url(r'^$', views.return_404),
        url(r'^login/?$', views.return_404),
        url(r'^signup/?$', views.return_404),
        url(r'^ask/?$', views.return_404),
        url(r'^popular/?$', views.return_404),
        url(r'^new/?$', views.return_404),
]