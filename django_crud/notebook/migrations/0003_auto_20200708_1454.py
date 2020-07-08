# Generated by Django 3.0.8 on 2020-07-08 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notebook', '0002_auto_20200708_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='draft_user',
            field=models.ForeignKey(db_column='draft_user', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='notebook',
            unique_together={('id', 'draft_user')},
        ),
    ]
