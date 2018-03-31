from django.db import models


class Robot(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    def __str__(self):
        return str(self.number) + ' | ' + self.name


class Pit(models.Model):
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE, null=True)
    line_auto = models.BooleanField(default=False)
    switch_auto = models.BooleanField(default=False)
    scale_auto = models.BooleanField(default=False)
    autonomous = models.IntegerField(default=0)
    climbing = models.IntegerField(default=0)
    switch = models.IntegerField(default=0)
    scale = models.IntegerField(default=0)
    vault = models.IntegerField(default=0)
    overall_impression = models.IntegerField(default=0)
    notes = models.TextField(blank=True, null=True)

    @classmethod
    def create_pit(cls, scout):
        new_pit = Pit()
        for data in scout:
            if data['name'] == 'robot':
                new_pit.robot_id = data['value']
            if data['name'] == 'line_auto':
                new_pit.line_auto = data['value']
            if data['name'] == 'switch_auto':
                new_pit.switch_auto = data['value']
            if data['name'] == 'scale_auto':
                new_pit.scale_auto = data['value']
            if data['name'] == 'autonomous':
                new_pit.autonomous = data['value']
            if data['name'] == 'climbing':
                new_pit.climbing = data['value']
            if data['name'] == 'switch':
                new_pit.switch = data['value']
            if data['name'] == 'scale':
                new_pit.scale = data['value']
            if data['name'] == 'vault':
                new_pit.vault = data['value']
            if data['name'] == 'overall_impression':
                new_pit.overall_impression = data['value']
            if data['name'] == 'notes':
                new_pit.notes = data['value']
        new_pit.save()


class Match(models.Model):
    auto_choices = (
        ('None', 'None'),
        ('Baseline', 'Baseline'),
        ('CenterSwitch', 'Center Switch'),
        ('SideSwitch', 'Side Switch'),
        ('Scale', 'Scale')
    )

    # team number - number
    robot = models.ForeignKey(Robot, on_delete=models.CASCADE, null=True)

    match_number = models.CharField(max_length=200)

    saturday = models.BooleanField(default=False)

    # Auton - selectable list(None, Baseline, Center switch, side switch, scale)
    auton = models.CharField(
        max_length=30,
        choices=auto_choices,
        default='None',
    )

    # auto cubes - number
    auto_cubes = models.IntegerField(default=0)

    # auto notes - string
    auto_notes = models.CharField(max_length=200, blank=True, null=True)

    # cubes in own switch - number
    own_switch_cubes = models.IntegerField(default=0)

    # cubes in opponents switch - number
    other_switch_cubes = models.IntegerField(default=0)

    # cubes in scale - number
    scale_cubes = models.IntegerField(default=0)

    # cubes in vault - number
    vault_cubes = models.IntegerField(default=0)

    # teleoperated notes - string
    tele_notes = models.CharField(max_length=200, blank=True, null=True)

    # Climbs - bool
    can_climb = models.BooleanField(default=False)

    # climbs with others - bool
    buddy_climb = models.BooleanField(default=False)

    # speed of robot - number (1-10)
    robot_speed = models.IntegerField(default=0)

    # Proficiency at Picking up Cubes - number (1-10)
    robot_cube_intake = models.IntegerField(default=0)

    # Proficiency at Keeping Hold of Cubes - number (1-10)
    robot_cube_holding = models.IntegerField(default=0)

    # Proficiency at Placing Cubes - number (1-10)
    robot_cube_placing = models.IntegerField(default=0)

    # additional notes - string
    other_notes = models.CharField(max_length=200, blank=True, null=True)

    # name of person who submitted report
    scouter_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Matches"

    def __str__(self):
        return str(self.robot.number) + " - match " + str(self.match_number)

    @classmethod
    def create_match(cls, scout):
        new_match = Match()
        for data in scout:
            if data['name'] == 'match_number' :
                new_match.match_number = data['value']
            if data['name'] == 'robot':
                new_match.robot_id = data['value']
            if data['name'] == 'auton':
                new_match.auton = data['value']
            if data['name'] == 'auton_cubes':
                new_match.auto_cubes = data['value']
            if data['name'] == 'auton_notes':
                new_match.auto_notes = data['value']
            if data['name'] == 'own_switch_cubes':
                new_match.own_switch_cubes = data['value']
            if data['name'] == 'other_switch_cubes':
                new_match.other_switch_cubes = data['value']
            if data['name'] == 'scale_cubes':
                new_match.scale_cubes = data['value']
            if data['name'] == 'vault_cubes':
                new_match.vault_cubes = data['value']
            if data['name'] == 'tele_notes':
                new_match.tele_notes = data['value']
            if data['name'] == 'can_climb':
                new_match.can_climb = data['valiue']
            if data['name'] == 'buddy_climb':
                new_match.buddy_climb = data['value']
            if data['name'] == 'robot_cube_intake':
                new_match.robot_cube_intake = data['value']
            if data['name'] == "robot_cube_holding":
                new_match.robot_cube_holding = data['value']
            if data['name'] == 'robot_cube_placing':
                new_match.robot_cube_placing = data['value']
            if data['name'] == 'other_notes':
                new_match.other_notes = data['value']
            if data['name'] == 'scouter_name':
                new_match.scouter_name = data['value']
        new_match.save()

        string = '[{"name":"team_number","value":"333"},' \
                 + '{"name":"match_number","value":"010"}]' \
                 + '{"name":"auton","value":"?????????????????????????????????????????????"}]' \
                 + '{"name":"auton_cubes","value":"455"}]' \
                 + '{"name":"auton_notes","value":"auto notes"}]' \
                 + '{"name":"own_switch_cubes","value":"455"}]' \
                 + '{"name":"other_switch_cubes","value":"455"}]' \
                 + '{"name":"scale_cubes","value":"455"}]' \
                 + '{"name":"vault_cubes","value":"455"}]' \
                 + '{"name":"tele_notes","value":"teleoperated notes"}]' \
                 + '{"name":"can_climb","value":"False"}]' \
                 + '{"name":"buddy_climb","value":"False"}]' \
                 + '{"name":"robot_speed","value":"455"}]' \
                 + '{"name":"robot_cube_intake","value":"455"}]' \
                 + '{"name":"robot_cube_holding","value":"455"}]' \
                 + '{"name":"robot_cube_placing","value":"455"}]' \
                 + '{"name":"other_notes","value":"other notes"}]' \
                 + '{"name":"scouter_name","value":"scouter"}]'
