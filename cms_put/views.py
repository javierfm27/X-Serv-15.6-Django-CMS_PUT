from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    if request.method == 'GET':
        return HttpResponse("Hacemos un GET")
    elif request.method == 'POS':
        return HttpResponse("Hacemos un POST")
