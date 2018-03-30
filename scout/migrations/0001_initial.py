# Generated by Django 2.0.3 on 2018-03-30 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_number', models.IntegerField(default=0)),
                ('match_number', models.CharField(max_length=200)),
                ('auton', models.CharField(choices=[('None', 'None'), ('Baseline', 'Baseline'), ('CenterSwitch', 'Center Switch'), ('SideSwitch', 'Side Switch'), ('Scale', 'Scale')], default='None', max_length=30)),
                ('auto_cubes', models.IntegerField(default=0)),
                ('auto_notes', models.CharField(blank=True, max_length=200, null=True)),
                ('own_switch_cubes', models.IntegerField(default=0)),
                ('other_switch_cubes', models.IntegerField(default=0)),
                ('scale_cubes', models.IntegerField(default=0)),
                ('vault_cubes', models.IntegerField(default=0)),
                ('tele_notes', models.CharField(blank=True, max_length=200, null=True)),
                ('can_climb', models.BooleanField(default=False)),
                ('buddy_climb', models.BooleanField(default=False)),
                ('robot_speed', models.IntegerField(default=0)),
                ('robot_cube_intake', models.IntegerField(default=0)),
                ('robot_cube_holding', models.IntegerField(default=0)),
                ('robot_cube_placing', models.IntegerField(default=0)),
                ('other_notes', models.CharField(blank=True, max_length=200, null=True)),
                ('scouter_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_number', models.IntegerField(default=0)),
                ('line_auto', models.BooleanField(default=False)),
                ('switch_auto', models.BooleanField(default=False)),
                ('scale_auto', models.BooleanField(default=False)),
                ('autonomous', models.IntegerField(default=0)),
                ('climbing', models.IntegerField(default=0)),
                ('switch', models.IntegerField(default=0)),
                ('scale', models.IntegerField(default=0)),
                ('vault', models.IntegerField(default=0)),
                ('overall_impression', models.IntegerField(default=0)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Robot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='pit',
            name='robot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scout.Robot'),
        ),
        migrations.AddField(
            model_name='match',
            name='robot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scout.Robot'),
        ),
    ]