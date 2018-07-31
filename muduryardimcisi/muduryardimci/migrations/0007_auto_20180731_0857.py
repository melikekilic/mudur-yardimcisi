# Generated by Django 2.0.7 on 2018-07-31 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('muduryardimci', '0006_auto_20180731_0849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='check_morning',
        ),
        migrations.AlterField(
            model_name='check',
            name='check_afternoon',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='check',
            name='check_evening',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='note',
            name='site_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Note_site_id', to='muduryardimci.Site'),
        ),
    ]