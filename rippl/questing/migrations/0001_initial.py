# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 02:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('legislature', '0004_auto_20161214_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField()),
                ('rep', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legislature.Representative')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='QuestAttempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField(null=True)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legislature.District')),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questing.Quest')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempts', models.IntegerField()),
                ('duration', models.DurationField()),
                ('quest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questing.Quest')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='quest',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questing.Topic'),
        ),
    ]