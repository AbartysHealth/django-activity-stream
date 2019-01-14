# Generated by Django 2.1.4 on 2019-01-14 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actstream', '0004_auto_20181129_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='parent_activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='children_activities', to='actstream.Action'),
        ),
    ]
