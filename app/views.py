from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse


# Create your views here.

def insert_dept(request):
    EDFO=Deptform()
    d={'EDFO':EDFO}

    if request.method=='POST':
        DFDO=Deptform(request.POST)
        if DFDO.is_valid():
            dn=DFDO.cleaned_data['dept_no']
            n=DFDO.cleaned_data['dname']
            l=DFDO.cleaned_data['location']

            DO=Dept.objects.get_or_create(dept_no=dn,dname=n,location=l)[0]
            DO.save()
            return HttpResponse('inserted successfully')
    
        else:
            return HttpResponse('invalid response')

    return render(request,'insert_deptform.html',d)

def insert_emp(request):
    EEFO=Empform()
    d={'EEFO':EEFO}
    if request.method=='POST':
        EFDO=Empform(request.POST)
        if EFDO.is_valid():
            dn=EFDO.cleaned_data['dept_no']
            DO=Dept.objects.get(dept_no=dn)
            e=EFDO.cleaned_data['emp_no']
            n=EFDO.cleaned_data['emp_name']

            EO=Emp.objects.get_or_create(dept_no=DO,emp_no=e,emp_name=n)[0]
            EO.save()
            return HttpResponse('inserted successfully')
    
        else:
            return HttpResponse('invalid response')

    return render(request,'insert_empform.html',d)
