from django.shortcuts import render,redirect
from .forms import FeesForm
from django.urls import reverse
from django.urls import reverse_lazy
from .models import StudentModel,FeesModel,ResourceProfile,Generalprofile
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from .forms import SignupR,SignupG
# Create your views here.

# def feesdata(request):
#     list=FeesModel.objects.all().order_by("Std_id")
#     context={
#         'access_records':list,
#     }
#     return render(request,'fees/feedata.html',context)

# def profiledata(request):
#     list=Profile.objects.all()
#     context={
#         'access_records':list,
#     }
#     return render(request,'profiles/profiledata.html',context)

class FeesCreateView(CreateView):
    model = FeesModel
    fields=('Name','Std_id','Receipt_no','Total_fees')
    template_name="fees/fee_form.html"
    success_url = reverse_lazy("feesdata")


class FeesUpdateView(UpdateView):
    model=FeesModel
    # success_url="/"
    fields=('Name','Std_id','Receipt_no','Total_fees')
    success_url = reverse_lazy("feesdata")

class FeesDeleteView(DeleteView):
    model=FeesModel
    success_url=reverse_lazy("feesdata")

class FeesDetailView(DetailView):
    model=FeesModel
    context_object_name="FeesModel"

def studentdata(request):
    lists=StudentModel.objects.all().order_by("Std_id")
    context = {
        'allstudent':lists
    }
    return render(request,'studentdata/studentdata.html',context)

class StudentCreateView(CreateView):
    model=StudentModel
    template_name="studentdata/createstudent.html"
    fields=('name','Class','Std_id','Mobile_no','Gender','Academic_year','Branch')
    success_url = reverse_lazy("studentdata")
class StudentUpdateView(UpdateView):
    model=StudentModel
    # success_url='/'
    fields=('name','Class','Std_id','Mobile_no','Gender','Academic_year','Branch')
    success_url = reverse_lazy("studentdata")


class StudentDetailView(DetailView):
    model=StudentModel
    context_object_name="student"


class StudentDeleteView(DeleteView):
    model=StudentModel
    success_url=reverse_lazy("studentdata")



def home(request):
    context = {"home_page": "active"}
    return render(request,'home.html',context)

def signupR(request):
    template_name="auth/signup.html"

    context={"title":"signup"}
    if request.method == 'POST':
        form=SignupR(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form= SignupR()

    context["form"]=form
    return render(request,template_name,context)
