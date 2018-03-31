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
        exclude = ['saturday']
        labels = {
            "scale_cubes": "Scale Cubes",
            "robot_speed" : "Robot Speed (rank from 1 to 10)",
            "robot_cube_holding" : "Robot skill at holding cubes(1 to 10) ",
            "robot_cube_intake" : "Robot skill at intaking cubes (1 to 10)",
            "robot_cube_placing" : "Robot skill at placing cubes (1 to 10)"
        }


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
