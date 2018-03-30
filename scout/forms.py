from django import forms

from .models import Robot, Pit, Match


class RobotForm(forms.ModelForm):
    class Meta:
        model = Robot
        fields = '__all__'


class PitForm(forms.ModelForm):
    class Meta:
        model = Pit
        fields = '__all__'


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = '__all__'


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
