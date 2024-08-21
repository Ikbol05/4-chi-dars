# Generated by Django 3.2.12 on 2024-08-01 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0003_recentarticles'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterBottom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_center', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('facebook_link', models.URLField(max_length=255)),
                ('Twitter_link', models.URLField(max_length=255)),
                ('likedIN_link', models.URLField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FooterBottomImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/foter_ottom')),
            ],
        ),
        migrations.RemoveField(
            model_name='banner',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='sub_title',
        ),
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.ImageField(upload_to='media/Banner'),
        ),
    ]