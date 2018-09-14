from django.http import HttpResponse
from .models import Center,User,Attendance
from django.template import loader
from django.shortcuts import render
from .forms import CheckBoxTest,CenterForm,UserChangeForm,UpdateForm,attendanceForm,DateForm,UpdateFormWithCenter
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def index(request):
    users = User.objects.all()
    template = loader.get_template('attendance/users.html')
    context = {
        'users' : users
    }
    return render(request,'attendance/users.html',context)

def user_details(request,user_id):
    user_detail_query = User.objects.filter(id=user_id)
    user_detail = user_detail_query.values()
    user_detail_dict = user_detail.get()
    context = {
        'user_detail' : user_detail_dict
    }
    return render(request,'attendance/user_details.html', context)

@login_required(login_url='/login/')
def checkboxview(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        centerform = CenterForm(request.POST)
        # print(centerform)
        # check whether it's valid:
        if centerform.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            data = centerform.cleaned_data
            center_name = data['your_choice']
            center_id_query = Center.objects.filter(center_name=center_name)
            center_data = center_id_query.values()[0]
            center_id = center_data['id']
            users = User.objects.filter(username_id=center_id)
            centerform = CenterForm()
            context = {
                'users': users,
                'center_name': center_name
            }
            return render(request, 'attendance/attendance.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        centerform = CenterForm()
#        userform = CheckBoxTest()
        users = User.objects.all()
        template = loader.get_template('attendance/users.html')
        context = {
            'users': users,
            'centerform' : centerform
        }

    return render(request, 'attendance/checkbox.html',context)


@login_required(login_url='/login/')
def update_attendance(request):
    if request.method == 'POST':
        update_form = UpdateForm(request.POST)
        #print (request.POST)
        # if update_form.is_valid():
        #     data = update_form.cleaned_data
        #     print(data)
        #     for user_id in data['selected_users']:
        #         user_obj = user.objects.get(pk=user_id)
        #         date = datetime.now()
        #         if attendance.objects.filter(user_id=user_id, date_id=date):
        #             pass
        #         else:
        #             update = attendance(user=user_obj,date_id=date)
        #             update.save()
        #         result = attendance.objects.all()
        #return HttpResponse(result.values())
        req = request.POST
        date = req['date_field_year'] + "-" + req['date_field_month'] + "-" + req['date_field_day']
        datetime_obj = datetime.strptime(date,"%Y-%m-%d")
        if req.getlist('options'):
            for user_id in req.getlist('options'):
                user_obj = User.objects.get(pk=user_id)
                if Attendance.objects.filter(user_id=user_id, date_id=date):
                    pass
                else:
                    update = Attendance(user=user_obj,date_id=datetime_obj)
                    update.save()
                result = Attendance.objects.all()
            return HttpResponse(result)
        else:
            center_id= req['selected_center']
            update_form = UpdateFormWithCenter(u=center_id)
            # update_form.selected_center = None
            context = {
                'users' : update_form,
            }
            return render(request,'attendance/update.html',context)
            #return HttpResponse("getting data")

    else:
        d = datetime.now()
        marked_attendance = Attendance.objects.filter(date_id=d)
        marked_attendance_list = [ u['user_id'] for u in marked_attendance.values() ]
        print ("**********",marked_attendance_list)
        update_form = UpdateForm(initial={'selected_users':marked_attendance_list})
        context = {
            'users' : update_form,
        }
        # print(update_form.__dict__)
        return render(request,'attendance/update.html',context)

def show_date(request):
    if request.method == "POST":
        date_form = DateForm(request.POST)
        if date_form.is_valid():
            data = date_form.cleaned_data
            #print (data['date_field'])
            return HttpResponse(data['date_field'])
    else:
        date_form = DateForm(user=None)
        context = {
            'date_form' : date_form
        }
        return render(request,'attendance/date.html',context)

