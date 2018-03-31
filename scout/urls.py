from django.urls import path

from . import views

urlpatterns = [
    # path('', views.simple_scout),
    path('add/match/', views.add_match, name='add_match'),
    path('add/pit/', views.add_pit, name='add_pit'),
    path('add/robots/', views.add_robots),
    path('add/external/', views.add_external),
    path('rank/', views.list_robots, name='rank'),
    path('rank/saturday/', views.list_saturday_robots, name='rank_saturday'),
    path('util/tally-to-count/', views.tally_to_count, name='tally-to-count'),
    # path('robot/<int:id>/', views.robot),
]
