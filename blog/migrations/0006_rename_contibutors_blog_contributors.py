# Generated by Django 4.2.4 on 2023-08-19 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='contibutors',
            new_name='contributors',
        ),
    ]
