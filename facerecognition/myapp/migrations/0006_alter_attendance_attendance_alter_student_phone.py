# Generated by Django 4.2.6 on 2024-01-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_attendance_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='Attendance',
            field=models.CharField(default='Present', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='Phone',
            field=models.BigIntegerField(),
        ),
    ]