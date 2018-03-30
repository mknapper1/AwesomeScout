from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Robot, Pit, Match

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
def add_match(request):
    return JsonResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def add_pit(request):
    return JsonResponse("Hello, world. You're at the polls index.")


@csrf_exempt
def add_robots(request):
    return JsonResponse("Hello, world. You're at the polls index.")


def list_robots(request):
    return JsonResponse("Hello, world. You're at the polls index.")
# return render(request, 'scouter/birdseyeview.html', {'my_surveys': my_surveys})


def rank_robots(request):
    return JsonResponse("Hello, world. You're at the polls index.")
    # return render(request, 'scouter/birdseyeview.html', {'my_surveys': my_surveys})

