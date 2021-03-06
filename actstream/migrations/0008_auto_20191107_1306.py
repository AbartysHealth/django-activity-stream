# Generated by Django 2.1.7 on 2019-11-07 17:06

import actstream.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0007_auto_20190629_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='action_object_object_id',
            field=actstream.models.CharField_ID(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='actor_object_id',
            field=actstream.models.CharField_ID(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='action',
            name='permission_object_id',
            field=actstream.models.CharField_ID(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='action',
            name='target_object_id',
            field=actstream.models.CharField_ID(blank=True, db_index=True, max_length=255, null=True),
        ),
    ]
