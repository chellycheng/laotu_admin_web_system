# Generated by Django 3.0.8 on 2020-08-05 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_datetime', models.DateTimeField(help_text='Enter datetime of event')),
                ('title', models.CharField(blank=True, help_text='Enter title of event', max_length=100, null=True)),
                ('location', models.CharField(blank=True, help_text='Enter the city location', max_length=60, null=True)),
                ('availability', models.CharField(blank=True, help_text='Enter the range of available dates', max_length=100, null=True)),
                ('speaker', models.CharField(blank=True, help_text='Enter speaker name', max_length=60, null=True)),
                ('discount_policy', models.CharField(blank=True, help_text='Enter discount policy', max_length=100, null=True)),
                ('description_picture', models.CharField(blank=True, help_text='Enter image description', max_length=60, null=True)),
                ('price_final', models.IntegerField(blank=True, help_text='Enter final price', null=True)),
            ],
            options={
                'ordering': ['-event_datetime'],
            },
        ),
    ]
