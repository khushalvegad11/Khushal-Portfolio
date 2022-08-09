"""wscubetech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wscubetech import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage-us', views.homepage,name = "homepage"),
    path('home-us', views.homeus,name = "home"),
    path('about-us/',views.aboutus,name = "about"),
    path('portfolio-us/',views.portfolio,name = "portfolio"),
    path('services-us/',views.service,name = "service"),
    path('resume-us/',views.resume,name = "resume"),
    path('blog-us/',views.blog,name = "blog"),
    path('contact-us/',views.contact,name = "contact"),
    path('user-us/',views.userform,name = "userform"),
    path('components-us/',views.components,name = "components"),
    path('calculator-us/',views.calculator,name = "calculator"),
    path('evenodd-us/',views.evenodd,name = "evenodd"),
    path('marksheet',views.marksheet,),
    path('newsdetails/<slug>', views.newsDetails,name = "newsDetails"),
    path('saveenquiry', views.saveEnquiry,name = "saveenquiry"),
    path('documents',views.documents,name = "documents"),

    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)