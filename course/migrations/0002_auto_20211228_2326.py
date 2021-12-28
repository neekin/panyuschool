# Generated by Django 3.2.9 on 2021-12-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='roomAddress',
            field=models.CharField(help_text='课室位置', max_length=255, verbose_name='课室位置'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='roomLoad',
            field=models.IntegerField(help_text='容纳人数', verbose_name='容纳人数'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='roomNumber',
            field=models.CharField(help_text='课室编码', max_length=100, verbose_name='课室编码'),
        ),
        migrations.AlterField(
            model_name='classroomorder',
            name='usage_curricula',
            field=models.TextField(help_text='使用理由', verbose_name='使用该课室理由'),
        ),
        migrations.AlterField(
            model_name='classroomorder',
            name='usage_user',
            field=models.CharField(help_text='预约人姓名', max_length=100, verbose_name='预约人姓名'),
        ),
    ]