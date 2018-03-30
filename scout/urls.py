from django.urls import path

from . import views

urlpatterns = [
    path('add/match/', views.add_match),
    path('add/pit/', views.add_pit),
    path('add/robots/', views.add_robots),
    path('list/', views.list),
    path('robot/<int:id>/', views.robot),
]
