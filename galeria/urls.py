from django.urls import path
from galeria.views import index, sobre

urlpatterns = [
          path('', index, name='index'),
          path('sobre/', sobre, name='sobre')
]          