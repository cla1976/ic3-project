# Generated by Django 4.1.7 on 2023-04-01 03:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=50)),
                ('date_purchased', models.DateField()),
                ('is_active', models.BooleanField(default=False)),
                ('is_synchronized', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_profile_api.device')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('male', 'Hombre'), ('female', 'Mujer'), ('unknown', 'Sin especificar')], max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('dni', models.CharField(max_length=100, null=True, unique=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('emergency_phone', models.CharField(max_length=100, null=True)),
                ('devices_total', models.CharField(choices=[('1', 'Device 1'), ('2', 'Device 2'), ('3', 'Device 3')], max_length=100)),
                ('beginTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
                ('fileImage', models.FileField(blank=True, upload_to='user_profile_api/images/')),
                ('userVerifyMode', models.CharField(choices=[('cardOrfaceOrPw', 'Tarjeta, cara o clave'), ('cardOrPw', 'Tarjeta o clave'), ('card', 'Tarjeta'), ('cardOrFace', 'Cara o clave'), ('face', 'Cara')], max_length=30)),
                ('timeType', models.CharField(default='local', max_length=10)),
                ('profile_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_profile_api.userprofiletype')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('análisis matematico', 'Análisis matemático'), ('física', 'Física'), ('química', 'Química')], max_length=100)),
                ('career', models.CharField(choices=[('computer engineering', 'Computer Engineering'), ('mechatronics', 'Mechatronics'), ('bioinformatics', 'Bioinformatics')], max_length=100)),
                ('begin_hour', models.CharField(choices=[('8', '8:00'), ('9', '9:00'), ('10', '10:00'), ('11', '11:00'), ('12', '12:00'), ('13', '13:00'), ('14', '14:00'), ('15', '15:00'), ('16', '16:00'), ('17', '17:00'), ('18', '18:00'), ('19', '19:00'), ('20', '20:00'), ('21', '21:00'), ('22', '22:00'), ('23', '23:00')], max_length=20)),
                ('end_hour', models.CharField(choices=[('8', '8:00'), ('9', '9:00'), ('10', '10:00'), ('11', '11:00'), ('12', '12:00'), ('13', '13:00'), ('14', '14:00'), ('15', '15:00'), ('16', '16:00'), ('17', '17:00'), ('18', '18:00'), ('19', '19:00'), ('20', '20:00'), ('21', '21:00'), ('22', '22:00'), ('23', '23:00')], max_length=20)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_profile_api.room')),
            ],
        ),
    ]
