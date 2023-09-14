from django.shortcuts import render

# Create your views here.
import datetime
def bif(request):
    dis='hi how are you'
    dt=datetime.datetime.now()
    d={'dis':dis,'dt':dt}
    return render(request,'bif.html',d)