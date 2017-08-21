# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('busshaming', '0007_auto_20170813_0429'),
    ]

    operations = [
        migrations.CreateModel(
            name='TripDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='busshaming.Trip')),
            ],
        ),
        migrations.RemoveField(
            model_name='triptimetable',
            name='trip',
        ),
        migrations.DeleteModel(
            name='TripTimetable',
        ),
        migrations.AlterUniqueTogether(
            name='tripdate',
            unique_together=set([('trip', 'date')]),
        ),
    ]