# Generated by Django 5.0.7 on 2024-08-02 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0005_banner_is_active_banner_sub_title_alter_banner_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footerbottom',
            old_name='Twitter_link',
            new_name='linkedin_link',
        ),
        migrations.RenameField(
            model_name='footerbottom',
            old_name='likedIN_link',
            new_name='twitter_link',
        ),
        migrations.AlterField(
            model_name='footerbottomimg',
            name='img',
            field=models.ImageField(upload_to='media/footer_bottom'),
        ),
    ]
