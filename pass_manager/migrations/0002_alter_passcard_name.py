# Generated by Django 3.2.5 on 2021-07-18 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pass_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passcard',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pass_manager.folder'),
        ),
    ]
