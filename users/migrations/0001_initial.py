# Generated by Django 5.1.1 on 2024-09-24 16:21

import django.contrib.auth.models
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(default='+996', max_length=14)),
                ('age', models.PositiveIntegerField(default=10, validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(5)])),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('level', models.CharField(choices=[('junior', 'Junior Developer'), ('middle', 'Middle Developer'), ('senior', 'Senior Developer')], default='junior', max_length=10)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
