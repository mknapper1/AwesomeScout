from django.urls import path

from . import views

urlpatterns = [
    # path('', views.simple_scout),
    path('add/match/', views.add_match, name='add_match'),
    path('add/pit/', views.add_pit, name='add_pit'),
    path('add/robots/', views.add_robots),
    path('add/external/', views.add_external),
    path('list/', views.list_robots, name='list'),
    path('rank/', views.rank_robots, name='rank'),
    path('util/tally-to-count', views.tally_to_count, name='tally-to-count'),
    # path('robot/<int:id>/', views.robot),
]
