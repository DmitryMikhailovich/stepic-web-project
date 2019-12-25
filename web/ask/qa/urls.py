from django.conf.urls import url

from . import views
app_name = 'qa'
urlpatterns = [
    url(r'^question/(?P<question_id>\d+)/?$', views.get_question, name='question'),
    url(r'^$', views.get_new),
    url(r'^login/?$', views.test),
    url(r'^signup/?$', views.test),
    url(r'^ask/?$', views.test),
    url(r'^popular/?$', views.get_popular, name='popular'),
    url(r'^new/?$', views.get_new, name='new'),
]
