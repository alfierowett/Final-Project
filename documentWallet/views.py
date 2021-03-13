from django.shortcuts import render
from django.http import HttpResponse



def documentWallet(request):
    return render(request, 'documentWallet/documentWallet.html')
