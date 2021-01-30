# Generated by Django 3.1.5 on 2021-01-30 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='percent_per_order',
            field=models.PositiveSmallIntegerField(default=0, help_text='%', verbose_name='Percent Per Order'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-Mail'),
        ),
    ]