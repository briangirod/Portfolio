# Generated by Django 4.0.5 on 2022-07-02 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Posteo',
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
