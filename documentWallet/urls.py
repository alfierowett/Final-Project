from django.urls import path
from . import views

#Set URL paths within the Document Wallet app

urlpatterns = [
    path('', views.documentWallet, name='documentWallet'),
    path('add/', views.newDocument, name='newDocument'),
    path('document/<str:pk>/', views.viewDocument, name='document'),
    path('deleteDocument/<str:pk>/', views.deleteDocument, name='deleteDocument'),
    path('AscWallet/', views.AscWallet, name='AscWallet'),
    path('DescWallet/', views.DescWallet, name='DescWallet'),
]

