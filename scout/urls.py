from django.urls import path

from . import views

urlpatterns = [
    path('', views.simple_scout),
    path('add/match/', views.add_match),
    path('add/pit/', views.add_pit),
    path('add/robots/', views.add_robots),
    path('add/external/', views.add_external),
    path('list/', views.list_robots),
    path('rank/', views.rank_robots),
    # path('robot/<int:id>/', views.robot),
]
