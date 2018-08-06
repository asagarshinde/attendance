from django import forms
from .models import user,center
from multiselectfield import MultiSelectField

class CheckBoxTest(forms.Form):
    users = user.objects.all()
    user_list = users.values()
    choice_list = [(value['initial'], value['initial']) for value in user_list]
    DISPLAY_CHOICES = tuple(choice_list)

    your_choice = forms.ChoiceField(widget=forms.RadioSelect, choices=DISPLAY_CHOICES)

class CenterForm(forms.Form):
    your_choice = forms.ModelMultipleChoiceField(widget=forms.RadioSelect, queryset=center.objects.all())