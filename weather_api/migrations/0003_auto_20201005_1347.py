# Generated by Django 3.1.2 on 2020-10-05 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weather_api', '0002_auto_20201005_1344'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Periods',
            new_name='Period',
        ),
        migrations.AddField(
            model_name='weatherrecord',
            name='period',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='period', to='weather_api.period'),
        ),
    ]
