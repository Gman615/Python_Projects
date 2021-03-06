# Generated by Django 3.1.4 on 2020-12-07 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default='', max_length=60)),
                ('last_name', models.CharField(blank=True, default='', max_length=60)),
                ('start_bal', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('type', models.CharField(choices=[('Deposit', 'Deposit'), ('Withdrawals', 'Withdrawals')], max_length=60)),
                ('amount', models.FloatField()),
                ('description', models.CharField(blank=True, default='', max_length=60)),
                ('account', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='Checkbook.account', verbose_name='Account')),
            ],
        ),
    ]
