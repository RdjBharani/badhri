# Generated by Django 4.0.2 on 2022-02-27 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('dob', models.DateField()),
            ],
            options={
                'db_table': 'user_details',
            },
        ),
    ]
