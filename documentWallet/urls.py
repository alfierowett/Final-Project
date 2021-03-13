from django.urls import path
from . import views

urlpatterns = [
    path('documentWallet/', views.documentWallet, name='documentWallet-home'),
]
