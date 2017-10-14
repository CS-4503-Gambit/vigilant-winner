# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 20:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judge_team',
            name='judge',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='core.Judge'),
        ),
        migrations.AlterField(
            model_name='judge_team',
            name='team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.Team'),
        ),
        migrations.AlterUniqueTogether(
            name='judge_team',
            unique_together=set([('judge', 'team')]),
        ),
    ]