from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_bible, name='search_bible'),
    path('<capitulo_numero>/<libro_name>', views.my_view, name='detailed_view'),
    
    # Other URL patterns...
]
