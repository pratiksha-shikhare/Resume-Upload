# Generated by Django 4.2.6 on 2024-01-02 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('locality', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('pincode', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('Pune', 'Pune'), ('Mumbai', 'Mumbai'), ('Banglore', 'Banglore'), ('Hyderabad', 'Hyderabad')], max_length=50)),
                ('mobile', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('job_city', models.CharField(max_length=100)),
                ('profile_image', models.ImageField(blank=True, upload_to='profileimg')),
                ('myfile', models.FileField(blank=True, upload_to='doc')),
            ],
        ),
    ]