# Generated by Django 4.0.4 on 2022-04-28 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='commentPost',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='commentUser',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='categoryPost',
        ),
        migrations.RemoveField(
            model_name='postcategory',
            name='categoryThrough',
        ),
        migrations.RemoveField(
            model_name='postcategory',
            name='postThrough',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='PostCategory',
        ),
    ]
