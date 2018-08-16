from django import forms
from django.forms import ModelForm
from .models import User,Center,Attendance
from multiselectfield import MultiSelectField
from datetime import datetime


class CheckBoxTest(forms.Form):
    users = User.objects.all()
    user_list = users.values()
    choice_list = [(value['initial'], value['initial']) for value in user_list]
    DISPLAY_CHOICES = tuple(choice_list)
    your_choice = forms.ChoiceField(widget=forms.RadioSelect, choices=DISPLAY_CHOICES)


class CenterForm(forms.Form):
    centers = Center.objects.all()
    center_obj = centers.values()
    center_list = [(ce['center_name'],ce['center_name']) for ce in center_obj ]
    selected_center = forms.CharField( widget=forms.Select(choices=tuple(center_list)))


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','initial')

    def __init__(self,*args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['user'].queryset = User.objects.all()

class UserListForm(forms.ModelForm):
    centers = forms.ModelChoiceField(queryset=Center.objects.all())
    users = forms.ModelChoiceField(queryset=User.objects.none())

    class Meta:
        model = Center
        fields = ('center_name', 'users')

class UpdateForm(forms.Form):
    date_field = forms.DateField(widget=forms.SelectDateWidget(),label='Joining Date', initial=datetime.now())
    centers = Center.objects.all()
    center_obj = centers.values()
    center_list = [(ce['id'],ce['center_name']) for ce in center_obj ]
    center_list.insert(0, (0, "Select center First"))
    selected_center = forms.CharField( widget=forms.Select(choices=tuple(center_list), attrs={'onchange': 'UpdateForm.submit();'}))
    users = User.objects.order_by('initial')
    user_list = users.values()
    choice_list = [(value['id'], str(value['initial']) + " " + str(value['last_name'])) for value in user_list]
    DISPLAY_CHOICES = tuple(choice_list)
    choices = [value['initial'] for value in user_list]
    selected_users = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=DISPLAY_CHOICES)

class UpdateFormWithCenter(forms.Form):

    def __init__(self,*args,**kwargs):
        center_id = kwargs.pop("u")
        super(UpdateFormWithCenter,self).__init__(*args,**kwargs)
        users = User.objects.filter(username_id=center_id)
        user_list = users.values()
        choice_list = [(value['id'], str(value['initial']) + " " + str(value['last_name'])) for value in user_list]
        self.DISPLAY_CHOICES = tuple(choice_list)
        self.fields['users'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=self.DISPLAY_CHOICES)

        self.fields['date_field'] = forms.DateField(widget=forms.SelectDateWidget(), label='Joining Date', initial=datetime.now())
        centers = Center.objects.all()
        center_obj = centers.values()
        center_list = [(ce['id'], ce['center_name']) for ce in center_obj]
        center_list.insert(0, (0, "Select center First"))
        center_list.pop(0)
        for i,t in enumerate(center_list):
            if str(center_id) == str(t[0]):
                first_element = center_list[0]
                center_list[0] = t
                center_list[i] = first_element
                print (center_list)
        self.fields['selected_center'] = forms.CharField(widget=forms.Select(choices=tuple(center_list),
                                                              attrs={'onchange': 'UpdateForm.submit();'}))


class attendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = ('id','user','date_id')
        widgets = {
            'user': forms.CheckboxSelectMultiple,
        }


class DateForm(forms.Form):
    date_field = forms.DateField(widget=forms.SelectDateWidget)
