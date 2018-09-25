from django.shortcuts import render
from .models import Content
import json

# Create your views here.

def test(request):
    if request.method == 'GET':

        return render(request,'Images/index.html')
def data(request):


    data = Content.objects.all()
    for i in data:
        d=  json.loads(str(i))
        print(d['name'])

    # write ths code:
    if request.method=='GET':
        return render(request,'Images/index.html',{'data':d['name']})






