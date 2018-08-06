from django.http import HttpResponse
from .models import center,user
from django.template import loader
from django.shortcuts import render
from .forms import CheckBoxTest,CenterForm

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


def checkboxview(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CenterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print (request)
            return HttpResponse("thanks")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CenterForm()

    return render(request, 'attendance/checkbox.html', {'form': form})
