from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.
class Curricula(models.Model):
    name = models.CharField(verbose_name='课程名称',max_length=100)
    description = models.TextField(verbose_name='课程介绍')
    teacher = models.CharField(verbose_name='授课老师',max_length=100)
    courseware = models.TextField(verbose_name='课件')
    class Meta:
        verbose_name ='课件管理'
        verbose_name_plural =verbose_name
    def __str__(self):
        return self.name


class Classroom(models.Model):
    room_number = models.CharField(verbose_name='课室编码',max_length=100,help_text='课室编码')
    room_address = models.CharField(verbose_name='课室位置',max_length=255,help_text='课室位置')
    room_load = models.IntegerField(verbose_name='容纳人数',help_text='容纳人数')
    def __str__(self):
        return self.room_number
    class Meta:
        verbose_name ='课室管理'
        verbose_name_plural =verbose_name

class ClassroomOrder(models.Model):
    ClassroomStatus = (
        (0, '未审核'),
        (1, '已审核'),
        (2, '已结束'),
    )
    classroom = models.ForeignKey(Classroom,verbose_name='预约课室',on_delete=models.DO_NOTHING,related_name='orders')
    usage_start_time = models.DateTimeField(verbose_name='开始使用时间')
    usage_end_time = models.DateTimeField(verbose_name='结束使用时间')
    usage_user = models.CharField(verbose_name='预约人姓名',help_text='预约人姓名',max_length=100)
    usage_curricula= models.TextField(verbose_name='使用该课室理由',help_text='使用理由')
    status = models.IntegerField(blank=True,choices=ClassroomStatus,default=0,null=True,verbose_name='状态')
    class Meta:
        verbose_name ='课室预约'
        verbose_name_plural =verbose_name