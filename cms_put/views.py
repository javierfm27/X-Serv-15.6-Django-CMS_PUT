from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    if request.method == 'GET':
        return HttpResponse("Hacemos un GET")
    elif request.method == 'POS':
        return HttpResponse("Hacemos un POST")


def mainPut(request):
    htmlAnswer = "<form id='paginas' method='put'>" \
        + "<label> Introduce el recurso y el contenido del recurso</br></label>" \
        + "<input name='recurso' type='text'>" \
        + "<input name='contenido' type='text'>" \
        + "<input type='submit' value='Enviar'></form>"
    return HttpResponse(htmlAnswer)
