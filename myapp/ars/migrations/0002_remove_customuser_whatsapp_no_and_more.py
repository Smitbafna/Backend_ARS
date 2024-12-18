# Generated by Django 5.1.2 on 2024-10-29 14:43

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='whatsapp_no',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='assign_reviewer_FK',
            field=models.ManyToManyField(blank=True, related_name='assignments_reviewed_by_member', to='ars.orgmember'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='assigned_teams_FK',
            field=models.ManyToManyField(to='ars.team'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='is_assign_creator_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments_created_by_member', to='ars.orgmember'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='start_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='assignmentsubtask',
            name='ass_to_subtask_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ars.assignment'),
        ),
        migrations.AlterField(
            model_name='assignmentsubtask',
            name='assign_subtask_reviewer_FK',
            field=models.ManyToManyField(to='ars.customuser'),
        ),
        migrations.AlterField(
            model_name='assignmentsubtask',
            name='assign_subtask_status_FK',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ars.submission'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='submission_id_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ars.submission'),
        ),
        migrations.AlterField(
            model_name='connectiondetails',
            name='user_id',
            field=models.ManyToManyField(to='ars.customuser'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='branch',
            field=models.CharField(choices=[], max_length=3),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(help_text='This field requires less than 320 characters.', max_length=320, validators=[django.core.validators.EmailValidator(), django.core.validators.RegexValidator(message='Email must be from @iitr.ac.in domain.', regex='^[\\w\\.-]+@iitr\\.ac\\.in$')]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='enr_no',
            field=models.IntegerField(help_text='This field requires exactly 8 digits.', validators=[django.core.validators.MinLengthValidator(8), django.core.validators.MaxLengthValidator(8)]),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(help_text='This field requires less than 255 characters.', max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profile_pic',
            field=models.FileField(upload_to='documents/profile_pics/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(help_text='This field requires less than 255 characters.', max_length=255),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='attach_feed_FK',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ars.attachment'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ars.customuser'),
        ),
        migrations.AlterField(
            model_name='orgmember',
            name='org_id_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ars.organization'),
        ),
        migrations.AlterField(
            model_name='orgmember',
            name='user',
            field=models.ManyToManyField(to='ars.customuser'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='reviewer_id_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ars.customuser'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='submission_status',
            field=models.CharField(choices=[('S', 'Submitted'), ('UR', 'Under Review'), ('C', 'Completed'), ('R', 'Rejected')], max_length=25),
        ),
        migrations.AlterField(
            model_name='submission',
            name='subtask_id_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ars.assignmentsubtask'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='team_leader_id_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ars.team'),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_leader_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams_led_by_member', to='ars.orgmember'),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_leader_submission_FK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ars.submission'),
        ),
        migrations.AlterField(
            model_name='team',
            name='team_members_FK',
            field=models.ManyToManyField(related_name='teams_with_member', to='ars.orgmember'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='Whatsapp_no',
            field=models.IntegerField(default=0, help_text='This field requires exactly 10 digits.', validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(10)]),
            preserve_default=False,
        ),
    ]
