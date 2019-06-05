"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLc  onf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import login,logout

from students.views import (home,signupR)
# FeesCreateView,FeesDetailView,
#                             FeesUpdateView,FeesDeleteView,StudentCreateView,
#                             StudentDetailView,StudentUpdateView,
                            # studentdata,StudentDeleteView,feesdata,
urlpatterns = [
    path('',home,name="home"),
    path('admin/', admin.site.urls),
    # path('fees/create/',FeesCreateView.as_view(),name='fees-create'),
    # path('fees/detail/<int:pk>',FeesDetailView.as_view(),name='fees-detail'),
    # path('fees/update/<int:pk>',FeesUpdateView.as_view(),name='fees-update'),
    # path('fees/delete/<int:pk>',FeesDeleteView.as_view(),name='fees-delete'),
    # path('student/create/',StudentCreateView.as_view(),name='student-create'),
    # path('student/detail/<int:pk>',StudentDetailView.as_view(),name="student-detail"),
    # path('student/update/<int:pk>',StudentUpdateView.as_view(),name="student-update"),
    # path('student/delete/<int:pk>',StudentDeleteView.as_view(),name="student-delete"),
    # path('student/data',studentdata,name="studentdata"),
    # path('fees/data',feesdata,name="feesdata"),
    # path('profile/data',profiledata,name="profiledata"),
    path('signup/',signupR,name='signup'),
    path('login/',login,{'template_name':'auth/login.html'},name='login'),
    path('logout/',logout,{'next_page':'/'},name='logout'),

]
