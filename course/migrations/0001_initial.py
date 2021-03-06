# Generated by Django 3.2.9 on 2021-12-09 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomNumber', models.CharField(max_length=100, verbose_name='课室编码')),
                ('roomAddress', models.CharField(max_length=255, verbose_name='课室位置')),
                ('roomLoad', models.IntegerField(verbose_name='容纳人数')),
            ],
            options={
                'verbose_name': '课室管理',
                'verbose_name_plural': '课室管理',
            },
        ),
        migrations.CreateModel(
            name='Curricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='课程名称')),
                ('description', models.TextField(verbose_name='课程介绍')),
                ('teacher', models.CharField(max_length=100, verbose_name='授课老师')),
                ('courseware', models.TextField(verbose_name='课件')),
            ],
            options={
                'verbose_name': '课件管理',
                'verbose_name_plural': '课件管理',
            },
        ),
        migrations.CreateModel(
            name='ClassroomOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usage_start_time', models.DateTimeField(verbose_name='开始使用时间')),
                ('usage_end_time', models.DateTimeField(verbose_name='结束使用时间')),
                ('usage_user', models.CharField(max_length=100, verbose_name='预约老师')),
                ('status', models.IntegerField(blank=True, choices=[(0, '未审核'), (1, '已审核'), (2, '已结束')], default=0, null=True, verbose_name='状态')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='course.classroom', verbose_name='预约课室')),
                ('usage_curricula', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='course.curricula', verbose_name='上课内容')),
            ],
            options={
                'verbose_name': '课室预约',
                'verbose_name_plural': '课室预约',
            },
        ),
    ]
