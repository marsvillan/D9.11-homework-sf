# Generated by Django 2.2.10 on 2020-09-12 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('D', 'draft'), ('P', 'published')], max_length=10)),
                ('content', models.TextField()),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Category')),
            ],
        ),
    ]
