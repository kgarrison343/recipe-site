from django.conf.urls import url

from . import views

app_name = 'recipes'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^menu/$', views.MenuView.as_view(), name='menu'),
    url(r'^(?P<recipe_id>[0-9]+)/toggle/$', views.toggle_on_the_menu, name='toggle'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
