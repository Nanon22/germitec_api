# Generated by Django 3.1.5 on 2021-01-12 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('general_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='heart.general')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Department',
                'ordering': ['id', 'name'],
            },
            bases=('heart.general',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('general_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='heart.general')),
                ('status', models.CharField(choices=[('admin', 'Administrator'), ('developer', 'Developer'), ('HRE', 'Humans Resources Employee'), ('secretary', 'Secretary'), ('trainee', 'Trainee')], default='trainee', max_length=32)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='persons', to='heart.department')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Person',
                'ordering': ['id'],
            },
            bases=('heart.general',),
        ),
    ]
