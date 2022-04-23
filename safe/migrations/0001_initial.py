# Generated by Django 4.0.4 on 2022-04-23 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('passwd', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Locker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=256)),
                ('username', models.CharField(max_length=30)),
                ('password', models.BinaryField()),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='safe.user', to_field='email')),
            ],
        ),
    ]
