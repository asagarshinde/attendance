from django.urls import path
from django.conf.urls import include

from . import views

app_name = 'attendance' # by defining app_name in template need to call url pattern like attendance:user_index for namespacing.

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:user_id>/', views.user_details, name='user_index'),
    path('checkbox/',views.checkboxview, name='user_list_view'),
    path('update/',views.update_attendance, name='update_user_attendance'),
    path('date/',views.show_date, name='show_date'),
]