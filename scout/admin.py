from django.contrib import admin

from .models import Robot, Pit, Match


class RobotAdmin(admin.ModelAdmin):
    list_display = ('robot',
                    'match_number',
                    'scale_cubes',
                    'vault_cubes',
                    'can_climb',
                    'created',
                    'updated')
    list_filter = ('robot', 'match_number')


admin.site.register(Robot, RobotAdmin)
admin.site.register(Pit)
admin.site.register(Match)
