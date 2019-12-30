from django.conf.urls import url

from . import views
app_name = 'qa'
urlpatterns = [
    url(r'^question/(?P<question_id>\d+)/?$', views.get_question, name='question'),
    url(r'^$', views.get_new),
    url(r'^login/?$', views.login_user, name='login'),
    url(r'^signup/?$', views.signup_new_user, name='signup'),
    url(r'^ask/?$', views.ask_question, name='ask'),
    url(r'^popular/?$', views.get_popular, name='popular'),
    url(r'^new/?$', views.get_new, name='new'),
]
