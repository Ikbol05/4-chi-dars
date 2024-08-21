# Generated by Django 5.0.7 on 2024-08-02 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0006_rename_twitter_link_footerbottom_linkedin_link_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SideMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('img', models.ImageField(upload_to='media/side_menu')),
            ],
        ),
    ]