# Generated by Django 3.1.2 on 2020-10-12 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_combination'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='actor',
            new_name='program',
        ),
        migrations.RenameField(
            model_name='entity',
            old_name='Tax_regno',
            new_name='Tax_reg_no',
        ),
        migrations.RenameField(
            model_name='entity',
            old_name='cont_no',
            new_name='contact_no',
        ),
        migrations.RenameField(
            model_name='entity',
            old_name='Reg_date',
            new_name='reg_date',
        ),
        migrations.RenameField(
            model_name='program',
            old_name='prog',
            new_name='entity',
        ),
        migrations.RenameField(
            model_name='program',
            old_name='no_ppl',
            new_name='no_of_people',
        ),
        migrations.RenameField(
            model_name='program',
            old_name='prog_name',
            new_name='programe_name',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='topic',
            new_name='program',
        ),
        migrations.RemoveField(
            model_name='entity',
            name='entity_id',
        ),
        migrations.AddField(
            model_name='entity',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]