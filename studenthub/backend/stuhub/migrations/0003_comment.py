# Generated by Django 4.1.7 on 2023-03-06 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stuhub', '0002_remove_course_coursecomments_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=100, verbose_name='Course Name')),
                ('professorRating', models.CharField(max_length=100, verbose_name='Prof Rating 1-10')),
                ('professorN', models.CharField(max_length=100, verbose_name='Professors Name')),
                ('courseComment', models.TextField(verbose_name='Comment')),
                ('commenterName', models.CharField(max_length=100, verbose_name='Commenters Name')),
            ],
        ),
    ]
