# Generated by Django 4.2.1 on 2023-06-03 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_rename_author_rating_author_rate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='rate',
            new_name='author_rating',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='post_author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='post_category',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='time_in',
            new_name='post_date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='rate',
            new_name='post_rating',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='article_text',
            new_name='post_text',
        ),
        migrations.RemoveField(
            model_name='post',
            name='head_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='type',
        ),
        migrations.AddField(
            model_name='post',
            name='post_choice',
            field=models.CharField(choices=[('AR', 'Статья'), ('NW', 'Новость')], default='NE', max_length=2),
        ),
        migrations.AddField(
            model_name='post',
            name='post_title',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
