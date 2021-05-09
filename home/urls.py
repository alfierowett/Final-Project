from django.urls import path
from . import views

#Set URL paths within the Homepage
urlpatterns = [
    path('', views.home, name='homepage-home'),
    path('usefulLinks/', views.links, name='usefulLinks')

]
