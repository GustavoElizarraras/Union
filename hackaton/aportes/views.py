from django.shortcuts import render
from .models import Aporte

# Create your views here.
def view_aportes(request):
    aportes_datos = Aporte.objects.all()
    
    return render(request,'aportes/aportes.html',{'datos':aportes_datos})
