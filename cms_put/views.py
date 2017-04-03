from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from cms_put.models import Pages

# Create your views here.
@csrf_exempt #SE UTILIZA PARA QUE NOS PERMITA REALIZAR EL POST
def main(request):
    if request.method == 'GET':
        htmlAnswer = "<form id='paginas' method='POST'>" \
            + "<label> Introduce el recurso y el contenido del recurso</br></label>" \
            + "<input name='name' type='text'>" \
            + "<br>" \
            + "<textarea name='page' rows='20' cols='100' ></textarea>" \
            + "<br>" \
            + "<input type='submit' value='Enviar'></form>"
        return HttpResponse(htmlAnswer)
    elif request.method == 'PUT':
        return HttpResponse("Hacemos un PUT")
    elif request.method == 'POST':
        recurso = request.POST['name']
        contenido = request.POST['page']
        pagina = Pages(name=recurso, page=contenido)
        pagina.save()
        return HttpResponse("Hacemos un POST" + request.body.decode('utf-8'))

def recurso(request, nombreRecurso):
    if request.method == 'GET':
        pagina = Pages.objects.get(name=nombreRecurso)
        return HttpResponse(pagina.page)
