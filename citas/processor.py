from citas.models import Cita, TipoCita
from blog.models import Employee

def getCitas(request):
    
    try:
        if request.user.employee:
            citas = Cita.objects.filter(employee_id=request.user.employee.id).all()
    except Exception as foo:
        citas = Cita.objects.filter(user=request.user.id).all()

    return {
        'citas': citas
    }

def getTypesOf(request):

    typesOf = TipoCita.objects.all()

    return {
        'typesOf': typesOf
    }

def getEmployees(request):
    employees = Employee.objects.all()
    return{
        'employees': employees
    }