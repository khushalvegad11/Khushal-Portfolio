from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import usersForm
from service.models import service
from news.models import News
from contactenquiry.models import contactEnquiry
from django.core.mail import send_mail

def homeus(request):
    newsData=News.objects.all()
    oo={
        'newsData': newsData,
    }
    return render(request,"index.html",oo)

def newsDetails(request,slug):
    
    newsDetails=News.objects.get(news_slug=slug)

    data={
        'newsDetails': newsDetails
    }
    return render(request,"newsdetails.html",data)



def homepage(request):
    return render(request,"header.html")

def calculator(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get("num1"))
            n2=eval(request.POST.get("num2"))
            opr=request.POST.get("opr")

            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2

    except:
        c="invalid opr......."
    print(c)

    return render(request,"calculator.html",{'c':c})

def aboutus(request):
    if request.method=='GET':
        output=request.GET.get("output")
    return render(request,"about.html",{'output':output})

def resume(request):
   
    return render(request,"resume.html")

def evenodd(request):
    c=''
    if request.method=="POST":
        if request.POST.get('num1')=="":
            return render(request,"evenodd.html",{'error':True})    

        n=eval(request.POST.get('num1'))
        if n%2==0:
            c="even number"
        else:
            c="odd number"

    return render(request,"evenodd.html",{'c':c})    

def components(request):
    return render(request,"components.html")

def portfolio(request):
    return render(request,"portfolio.html")

def marksheet(request):
    if request.method=="POST":
        s1=eval(request.POST.get('subject1'))
        s2=eval(request.POST.get('subject2'))
        s3=eval(request.POST.get('subject3'))
        s4=eval(request.POST.get('subject4'))
        s5=eval(request.POST.get('subject5'))
        t=s1+s2+s3+s4+s5
        p=t*100/500
        if p>=60:
            d="First Div"
        elif p>=48:
            d="Seciond Div"
        elif p>=35:
            d="Third Div"
        else:
            d="Fail"
        data={
            'total':t,
            'per':p,
            'div':d
        }
        
        return render(request,"marksheet.html",data)
    return render(request,"marksheet.html")


def contact(request):
    return render(request,"contact.html")

def saveEnquiry(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        en=contactEnquiry(name=name,email=email,message=message)
        en.save()
        n='Data inserted'

    return render(request,"contact.html",{'n':n})


def service(request):
    serviceData= service.objects.all()
    if request.method=="GET":
        st= request.GET.get('servicename')
        if st!=None:
            serviceData= service.objects.filter(service_title__icontains=st)

    data ={
          'serviceData': serviceData,

    }
    return render(request,"services.html",data)

def blog(request):
    return render(request,"blog.html")

def documents(request):
    return render(request,"index.html")


def courseid(request,courseid):
    return render(courseid)

def userform(request):
    finalans= 0
    fn=usersForm()

    data={'form':fn}
    try:
        if request.method == "POST":
        #n1=int(request.GET["num1"])
        #n2=int(request.GET["num2"])
            n1=int(request.POST.get("num1"))
            n2=int(request.POST.get("num2"))
            n3=int(request.POST.get("num3"))

            finalans=n1+n2
            data={

                'form':fn,
                'output': finalans
            }

            url="/about-us/? output={}".format(finalans)

            return redirect(url)
    except:
        pass
    return render(request,"userform.html",data)
