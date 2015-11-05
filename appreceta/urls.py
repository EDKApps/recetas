from django.conf.urls import patterns, include, url
from .views import RecipeCreateView

urlpatterns = patterns('',
  url(r'^appreceta/crear/$', RecipeCreateView.as_view(), name='receta_crear'),
)