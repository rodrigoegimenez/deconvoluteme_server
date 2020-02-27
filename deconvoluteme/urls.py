from django.urls import path
from . import views

urlpatterns = [
    path('deconvolute/', views.DeconvoluteMe.as_view(), name='deconvolute'),
]