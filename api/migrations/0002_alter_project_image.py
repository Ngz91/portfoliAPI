# Generated by Django 4.0 on 2022-06-02 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='projects/%Y/%m/%d', verbose_name="Project's image"),
        ),
    ]
