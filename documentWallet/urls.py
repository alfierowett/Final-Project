from django.urls import path
from . import views

urlpatterns = [
    path('', views.documentWallet, name='documentWallet'),
    path('add/', views.newDocument, name='newDocument'),
    path('document/<str:pk>/', views.viewDocument, name='document'),
    path('deleteDocument/<str:pk>/', views.deleteDocument, name='deleteDocument'),
]

