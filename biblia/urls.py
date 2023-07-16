from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('get-chapters', views.get_chapters, name='get_chapters'),
    path('get-verses', views.get_verses, name='get_verses'),
]
