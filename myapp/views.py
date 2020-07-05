from django.shortcuts import render
from myapp.models import School
# from myapp.forms import Login
from myapp.forms import UserForms
# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def stud(request):
    s = School.objects.order_by('student_class')
    stu = {'stu_data':s}
    return render(request, 'myapp/stud.html', context=stu)

# def log(request):
#     form = Login()
#     if request.method == "POST":
#         form = Login(request.POST)
#         if form.is_valid():
#             print("this is a valid form")
#             print('Name: '+form.cleaned_data['name'])
#             print('Email: '+form.cleaned_data['email'])
#             print('Text: '+form.cleaned_data['comments'])
#             print('Password: '+form.cleaned_data['password'])
#     return render(request, 'myapp/login.html', {'form':form})

def userforms(request):
    form = UserForms()
    if request.method == "POST":
        form = UserForms(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return home(request)
        else:
            print("ERROR!!")
    return render(request, 'myapp/userforms.html', {'form':form})
