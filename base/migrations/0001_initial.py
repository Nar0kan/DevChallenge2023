# Generated by Django 4.2.5 on 2023-10-04 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('cell_key', models.CharField(max_length=8, primary_key=True, serialize=False, unique=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.sheet')),
            ],
        ),
    ]
