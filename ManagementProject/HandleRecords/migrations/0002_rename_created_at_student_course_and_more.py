# Generated by Django 4.2.5 on 2023-09-12 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HandleRecords', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='created_at',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='address',
            new_name='father_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='last_name',
            new_name='roll_number',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='updated_at',
            new_name='semester',
        ),
        migrations.RemoveField(
            model_name='student',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone_number',
        ),
    ]
