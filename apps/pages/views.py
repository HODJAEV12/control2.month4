from django.shortcuts import render
from apps.config.models import CompanyInfo, Service

def index(request):
    company = CompanyInfo.objects.first()
    service = Service.objects.all()
    return render(request, "index.html", locals())

def catalog(request):
    return render(request, "catalog.html", locals())