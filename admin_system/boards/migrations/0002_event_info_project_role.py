# Generated by Django 3.0.8 on 2020-08-05 18:24

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(max_length=400)),
                ('descriptions', models.TextField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=400)),
                ('description', models.TextField(max_length=4000)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now_add=True)),
                ('localtion', models.TextField(max_length=1000)),
                ('price', models.IntegerField()),
                ('discount_policy', models.TextField(max_length=4000)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('category', models.CharField(choices=[('SS', 'SeniourStaff'), ('JS', 'JuniorStaff'), ('SK', 'Speaker')], default='JS', max_length=2)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=400)),
                ('notes', models.TextField(max_length=2000)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now_add=True)),
                ('localtion', models.TextField(max_length=1000)),
                ('speaker', models.TextField(max_length=2000)),
                ('Project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='events', to='boards.Project')),
            ],
        ),
    ]
