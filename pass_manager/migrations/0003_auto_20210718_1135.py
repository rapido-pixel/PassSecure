# Generated by Django 3.2.5 on 2021-07-18 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pass_manager', '0002_alter_passcard_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='passcard',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pass_manager.folder'),
        ),
        migrations.AlterField(
            model_name='passcard',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
