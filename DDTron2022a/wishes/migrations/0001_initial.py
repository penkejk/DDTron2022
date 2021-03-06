# Generated by Django 4.0.2 on 2022-02-15 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('people', '0001_initial'),
        ('events', '0002_event_desciption_event_event_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wish_text', models.TextField()),
                ('assigned_to', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assigned_rel', to='people.person')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='author_rel', to='people.person')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='events.event')),
            ],
        ),
    ]
