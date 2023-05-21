# Generated by Django 4.1.1 on 2023-04-02 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yogaapp', '0011_coursepurchase'),
        ('schedule', '0012_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classschedule',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_schedules', to='yogaapp.courses'),
        ),
    ]
