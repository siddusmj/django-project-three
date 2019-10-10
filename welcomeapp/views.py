from django.shortcuts import render
from .models import create

# Create your views here.
#welcomepge
def index(req):
    
    return render(req,'index.html')

def signup(request):
    return render(request,'signup.html')   

def ins(request):
    return render(request,'ins.html')    

def readData(req):
    name = req.GET['user']
    cname = req.GET['cname']
    cost = req.GET['cost']
    stu = create (name = name, usn = usn, marks = marks)
    stu.save()
    return render(req,'displayData.html')         
    

def displayData(req):   
    stusdata = create.objects.all()
    print(stusdata)
    for student in stusdata:
        print(student.name)
        print(student.cname)
        print(student.cost)
        print('---------------------------')
    context = {'studentData':stusdata} 
    return render(req,'displayData.html',context)

def getData(req):
    name = req.GET['uname']
    stu = create.objects.get(name = name)
    print(stu.name,stu.cname,stu.cost)
    return render(req,'index.html')


def updateData(req):
    name = req.GET['name']
    uusn = req.GET['updateusn']
      
      #
      #  markss = req.GET['mark']
      #
    stu = create.objects.get(name=name)
    stu.usn = uusn
    stu.save()

    return render(req,'index.html')

def deleteData(req):
    name = req.GET['name']
    stu = create.objects.get(name=name)    
    stu.delete()

    return render(req,'index.html')    