# Generated by Django 3.0.6 on 2021-10-13 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.IntegerField()),
                ('option_one', models.CharField(max_length=100)),
                ('option_two', models.CharField(max_length=100)),
                ('option_three', models.CharField(max_length=100)),
                ('option_four', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('confirm_password', models.CharField(max_length=100)),
            ],
        ),
    ]
