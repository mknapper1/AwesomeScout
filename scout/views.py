import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt

from .models import Robot, Pit, Match
from .forms import UploadFileForm, RobotForm, PitForm, MatchForm

# Create your views here.
# urlpatterns = [
#     path('add/match/', views.add_match),
#     path('add/pit/', views.add_pit),
#     path('add/robots/', views.add_robots),
#     path('list/', views.list),
#     path('robot/<int:id>/', views.robot),
# ]
#


@csrf_exempt
def simple_scout(request):
    return render(request, 'scout/simple_scout.html', {})


@csrf_exempt
def add_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            form = MatchForm()
    else:
        form = MatchForm()
    return render(request, 'scout/form.html', {'form': form})


@csrf_exempt
def add_pit(request):
    if request.method == 'POST':
        form = PitForm(request.POST)
        if form.is_valid():
            form.save()
            form = PitForm()
    else:
        form = PitForm()
    return render(request, 'scout/form.html', {'form': form})


@csrf_exempt
def add_robots(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            for chunk in request.FILES['file'].chunks():
                arr = str(chunk).split(',')
                for i in range(0, len(arr), 2):
                    # lazy hack
                    if arr[i][0] == 'b':
                        arr[i] = arr[i][2:]
                    robot = Robot(number=int(arr[i]), name=arr[i+1], slug=slugify(arr[i+1]))
                    robot.save()
                    print(robot)

            return JsonResponse({'status': 'ok'})
    else:
        form = UploadFileForm()
    return render(request, 'scout/form.html', {'form': form})


@csrf_exempt
def add_external(request):
    if request.method == 'POST':
            scout = json.loads(request.POST['scout'])
            for data in scout:
                name = data['name']
                value = data['value']
                if name == 'scout_type':
                    if value == 'match':
                        Match.create_match(scout)
                    if value == 'pit':
                        Pit.create_pit(scout)
            return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})


def list_robots(request):
    robots = Robot.objects.filter(match_data__isnull=False).distinct()
    return render(request, 'scout/list.html', {'robots': robots})
# return render(request, 'scouter/birdseyeview.html', {'my_surveys': my_surveys})


def list_saturday_robots(request):
    robots = Robot.objects.filter(match_data__saturday=True).distinct()
    return render(request, 'scout/list.html', {'robots': robots})


def tally_to_count(request):
    matches = Match.objects.all()
    for match in matches:
        if str(match.scale_cubes)[0] == '1':
            match.scale_cubes = len(str(match.scale_cubes))
        if str(match.vault_cubes)[0] == '1':
            match.vault_cubes = len(str(match.vault_cubes))
        if str(match.own_switch_cubes)[0] == '1':
            match.own_switch_cubes = len(str(match.own_switch_cubes))
        if str(match.other_switch_cubes)[0] == '1':
            match.other_switch_cubes = len(str(match.other_switch_cubes))
        match.save()
    return JsonResponse({"Status":"Done!"})


