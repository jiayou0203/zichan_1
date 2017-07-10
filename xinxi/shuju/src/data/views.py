# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.db import models
# Create your views here.
#from data.models import DataBlogspost
#from data.models import DataXinxisouji
from django.shortcuts import render_to_response
#from data.models import DataBlogUser
from data.models import BlogUser
from django.shortcuts import HttpResponse
from data.models import data
#from data.models import data_nei
from django.http import HttpResponseRedirect
def index(request):
    blog_list=data.objects.all()
    return render_to_response('blog.html',{'blog_list':blog_list})
    
#def xinxi(request):
#    xinxi_list=data.objects.all().values('nei_ip')
#    return render_to_response('blog.html',{'xinxi_list':xinxi_list})

#def test_data(request):
#    test_list=data.objects.all().values('wai_ip')
#    return render_to_response('blog.html',{'test_list':test_list})

#def data_shuju(request):
#    data_list=data_nei.objects.all()
#    return render_to_response('blog.html',{'test_list':data_list})
    
def dataid(request):
    import models
    body_list=DataXinxisouji.objects.all().values('pctiemstamp')
    return render(request,'data.html',{'body_list':body_list})    

def login(request):  
    error_msg=""
    import models
    if request.method=='POST':
        a_data_applicant=request.POST['applicant']
        a_data_department=request.POST['department']
        a_data_application_time=request.POST['application_time']
        a_data_internal_ip=request.POST.getlist('internal_ip',[])
        a_data_external_ip=request.POST.getlist('external_ip',[])
        a_data_application_brief=request.POST.getlist('application_brief',[]) 
        a_data_check_box=request.REQUEST.getlist('Fruit')
        a_url=request.REQUEST.getlist('url')
        a_agent=request.REQUEST.getlist('agent')
        a_white_list=request.REQUEST.getlist('white_list')
#        xinxi_list=data.objects.all()
#        models.data.objects.create(data_applicant=a_data_applicant,data_department=a_data_department,data_application_time=a_data_application_time,data_internal_ip=a_data_internal_ip,data_external_ip=a_data_external_ip,data_application_brief=a_data_application_brief)
        for i in range(0,len(a_data_internal_ip)):
            models.data.objects.create(data_applicant=a_data_applicant,data_department=a_data_department,data_application_time=a_data_application_time,data_internal_ip=a_data_internal_ip,data_external_ip=a_data_external_ip,data_application_brief=a_data_application_brief,nei_ip=a_data_internal_ip[i], checkbox_stat=a_data_check_box,wai_ip=a_data_external_ip[i],yont_tu=a_data_application_brief[i],url=a_url,agent=a_agent,white_list=a_white_list)

            
#        for i in range(0,len(a_data_external_ip)):
#            models.data.objects.create(wai_ip=a_data_internal_ip[i])
            
        if a_data_applicant=='root' and a_data_department=='123456':
           error_msg="登录成功"
        elif a_data_applicant=="":
           error_msg="用户名为空"
        elif a_data_department=="":
           error_msg="密码为空"
    return render(request,"login.html",{'error_msg':error_msg})
       
        
    user_list=models.data.objects.all()
    return render_to_response('blog.html',{'user_list':user_list})

def addline(request):
    return render(request,"addline.html")


def hello(request):
    return render(request,"hello.html")

def option(request):
    return render(request,"option.html")
            