# Generated by Django 4.2.6 on 2023-12-11 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_age_student_student_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_index_no',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
