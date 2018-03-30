from django.forms import ModelForm

from .models import Robot, Pit, Match


class RobotForm(ModelForm):
    class Meta:
        model = Robot
        fields = '__all__'


class PitForm(ModelForm):
    class Meta:
        model = Pit
        fields = '__all__'


class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = '__all__'
