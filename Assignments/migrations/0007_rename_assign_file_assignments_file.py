# Generated by Django 4.2.1 on 2023-06-01 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Assignments', '0006_alter_assignments_assign_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignments',
            old_name='assign_file',
            new_name='file',
        ),
    ]
