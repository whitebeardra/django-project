# Generated by Django 4.2.3 on 2023-08-04 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_rename_title_post_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
