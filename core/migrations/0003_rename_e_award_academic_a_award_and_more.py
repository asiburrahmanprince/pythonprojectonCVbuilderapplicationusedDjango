# Generated by Django 4.1.5 on 2023-01-29 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cv_skill_reference_profile_experince_academic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academic',
            old_name='e_award',
            new_name='a_award',
        ),
        migrations.RenameField(
            model_name='academic',
            old_name='e_year',
            new_name='a_year',
        ),
    ]
