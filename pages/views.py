from django.shortcuts import render
from .models import Page
from django.contrib.auth.decorators import login_required
from citas.models import Cita, TipoCita
from blog.models import Employee
from django.db import connection

# Create your views here.

@login_required(login_url="login")
def getPage(request,slug):

    page = Page.objects.filter(visible=True).get(slug=slug)

    return render(request, "pages/page.html", {
        'page': page
    })

@login_required(login_url="login")
def crudCita(request):
    if request.method == "POST":
        datetime = f"{request.POST.get('date')} {request.POST.get('time')}"
        idTipoCita = int(request.POST.get('tipoCita'))
        idProfesional = int(request.POST.get('profesional'))
        if request.POST.get('btn-agregar') and request.POST.get('time') != "":
            cita = Cita(date=datetime,user_id=request.user.id,employee_id=idProfesional,typeof_id=idTipoCita)
            cita.save()
        elif request.POST.get('btn-editar'):
            idCita = int(request.POST.get('idCita'))
            employee = Employee.objects.get(pk=idProfesional)
            typeOf = TipoCita.objects.get(pk=idTipoCita)
            cita = Cita.objects.get(pk=idCita)
            cita.employee = employee
            cita.typeof = typeOf
            cita.date = datetime
            cita.save()
        elif request.POST.get('btn-eliminar'):
            idCita = int(request.POST.get('idCita'))
            cita = Cita.objects.get(pk=idCita)
            cita.delete()

        page = Page.objects.filter(visible=True).get(slug='cita')
        return render(request, "pages/page.html", {
            'page': page
        })

@login_required(login_url="login")
def processCita(request):
    if request.method == "POST":
        idCita = int(request.POST.get('idCita'))
        cita = Cita.objects.get(pk=idCita)
        cita.comments = request.POST.get('comentarios')
        if request.POST.get('btn-aceptar'):
            cita.status = 1
        else:
            cita.status = 0
        cita.save()
    page = Page.objects.filter(visible=True).get(slug='cita')
    return render(request, "pages/page.html", {
        'page': page
    })

