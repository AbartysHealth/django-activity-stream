# Generated by Django 2.1.3 on 2018-11-29 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('actstream', '0003_add_follow_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='parent_activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='actstream.Action'),
        ),
        migrations.AddField(
            model_name='action',
            name='permission_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_permission', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='action',
            name='permission_object_id',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
    ]
