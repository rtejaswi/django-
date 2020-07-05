from django.contrib import admin
from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('sdata/',views.stud, name= 'stud' ),
    #path('login/', views.log, name = 'log'),
    path('userforms/', views.userforms, name = 'userforms'),
]
