from django.http import HttpResponse
from .models import center,user
from django.template import loader
from django.shortcuts import render

def index(request):
    users = user.objects.all()
    template = loader.get_template('attendance/users.html')
    context = {
        'users' : users
    }
    print(request)
    print(dir(request))
    return render(request,'attendance/users.html',context)

def user_details(request,user_id):
    user_detail_query = user.objects.filter(id=user_id)
    user_detail = user_detail_query.values()
    user_detail_dict = user_detail.get()
    context = {
        'user_detail' : user_detail_dict
    }
    return render(request,'attendance/user_details.html', context)
