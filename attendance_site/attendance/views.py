from django.http import HttpResponse
from .models import center,user

def index(request):
    users = user.objects.all()
    user_list = ','.join(u.initial for u in users)
    return HttpResponse(user_list)