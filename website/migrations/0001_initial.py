# Generated by Django 4.0.3 on 2022-04-23 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditorStatusChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=254)),
                ('lead', models.CharField(blank=True, max_length=254, null=True)),
                ('participants', models.TextField(max_length=500)),
                ('start_date', models.DateField(max_length=254, null=True)),
                ('end_date', models.DateField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventDurationChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='EventStatusChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='EventTypeChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='HardDrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('serial_number', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('model_number', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('connection_port', models.CharField(max_length=50)),
                ('classification_change_justification', models.TextField(blank=True, null=True)),
                ('image_version_ID', models.CharField(blank=True, max_length=10, null=True)),
                ('boot_test_expiration_date', models.DateField(blank=True, null=True)),
                ('hard_drive_status_change_justification', models.TextField(blank=True, null=True)),
                ('date_issued', models.DateField(blank=True, null=True)),
                ('expected_return_date', models.DateField(blank=True, null=True)),
                ('hard_drive_return_date_justification', models.TextField(blank=True, null=True)),
                ('actual_return_date', models.DateField(blank=True, null=True)),
                ('date_modified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HardDriveBootTestStatusChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='HardDriveClassificationChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='HardDriveSizeChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='HardDriveStatusChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='MaintainerStatusChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='RequesterStatusChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='RequestStatusChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(default='default.jpg', upload_to='')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('direct_supervisor_email', models.EmailField(max_length=254)),
                ('branch_chief_email', models.EmailField(max_length=254)),
                ('auditor_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.auditorstatuschoice')),
                ('maintainer_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.maintainerstatuschoice')),
                ('requester_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.requesterstatuschoice')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_number', models.CharField(max_length=22)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('date_of_last_modification', models.DateField(auto_now=True)),
                ('pickup_date', models.DateField(max_length=254, null=True)),
                ('number_of_classified_hard_drives_needed', models.PositiveIntegerField(default=0)),
                ('number_of_unclassified_hard_drives_needed', models.PositiveIntegerField(default=0)),
                ('comment', models.TextField(blank=True, null=True)),
                ('event', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.event')),
                ('hard_drive', models.ManyToManyField(blank=True, to='website.harddrive')),
                ('requester', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.userprofile')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.requeststatuschoice')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='harddrive',
            name='boot_test_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.harddrivebootteststatuschoice'),
        ),
        migrations.AddField(
            model_name='harddrive',
            name='classification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.harddriveclassificationchoice'),
        ),
        migrations.AddField(
            model_name='harddrive',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.harddrivesizechoice'),
        ),
        migrations.AddField(
            model_name='harddrive',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.harddrivestatuschoice'),
        ),
        migrations.AddField(
            model_name='event',
            name='duration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.eventdurationchoice'),
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.eventstatuschoice'),
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.eventtypechoice'),
        ),
    ]
