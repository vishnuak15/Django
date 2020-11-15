# Generated by Django 3.1.2 on 2020-10-12 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='Name',
            field=models.CharField(max_length=294),
        ),
        migrations.CreateModel(
            name='Funtions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fun_name', models.CharField(max_length=294, unique=True)),
                ('fun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.program')),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=294)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first_app.program')),
            ],
        ),
    ]