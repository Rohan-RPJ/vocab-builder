# Generated by Django 2.0.13 on 2019-03-17 20:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_lword_no', models.IntegerField(default=0)),
                ('current_rword_no', models.IntegerField(default=0)),
                ('category', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='progress',
            name='word_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='study.WordList'),
        ),
    ]
