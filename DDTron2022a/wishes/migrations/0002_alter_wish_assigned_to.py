# Generated by Django 4.0.2 on 2022-02-15 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('wishes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='assigned_to',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assigned_rel', to='people.person'),
        ),
    ]
