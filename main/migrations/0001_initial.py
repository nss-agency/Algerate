# Generated by Django 2.2.2 on 2019-06-28 12:55

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img', verbose_name='Image')),
                ('unique_link', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('isVerified', models.BooleanField(default=False, verbose_name='Verified')),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('ratedImage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.PostedImage')),
            ],
        ),
    ]
