from django.shortcuts import render
from django.http import HttpResponse
import datetime


def home(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    data = {}
    data['transacoes'] = ['T1','T2','T3','T4']
    data['now'] = datetime.datetime.now()
    return render(request,'contas/home.html', data)
