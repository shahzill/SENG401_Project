# Generated by Django 4.1.7 on 2023-03-18 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuhub', '0006_alter_professor_profid_alter_tutor_tutorid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='courseComments',
        ),
    ]
