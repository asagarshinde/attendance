from django.urls import path

from . import views

app_name = 'attendance' # by defining app_name in template need to call url pattern like attendance:user_index for namespacing.

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:user_id>/', views.user_details, name='user_index'),
]