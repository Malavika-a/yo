# Generated by Django 4.1.1 on 2023-03-29 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yogaapp', '0006_alter_courses_course_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredstudent',
            name='student_image',
            field=models.ImageField(default='', unique=True, upload_to='profile_image/'),
        ),
    ]
