from django.contrib import admin

from .models import Robot, Pit, Match


class MatchAdmin(admin.ModelAdmin):
    list_display = ('robot',
                    'match_number',
                    'scale_cubes',
                    'vault_cubes',
                    'own_switch_cubes',
                    'other_switch_cubes',
                    'can_climb')
    list_filter = ('robot', 'match_number')


admin.site.register(Robot)
admin.site.register(Pit)
admin.site.register(Match, MatchAdmin)
