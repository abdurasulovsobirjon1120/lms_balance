# Generated by Django 5.1.4 on 2024-12-14 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_balance', '0002_alter_student_first_name_alter_student_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[("to'langan", "To'langan"), ('qarzdor', 'Qarzdor')], default="to'langan", max_length=20),
        ),
    ]
