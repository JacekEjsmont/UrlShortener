from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('process_url', views.process_url, name='process_url'),
    path('<str:short>', views.open_shorten_url, name='open_shorten_url')
]
