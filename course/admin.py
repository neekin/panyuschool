from django.contrib import admin

# Register your models here.
admin.AdminSite.site_title = "番禺职业技术学校职业体验系统"
admin.site.site_header = "番禺职业技术学校体验系统"

from .models import Curricula,Classroom,ClassroomOrder

class CurriculaAdmin(admin.ModelAdmin):
    list_display =['name','teacher']

class ClassroomAdmin(admin.ModelAdmin):
    list_display =['room_number','room_address','room_load']

class ClassroomOrderAdmin(admin.ModelAdmin):
    list_display =['classroom','usage_start_time','usage_end_time','usage_user','usage_curricula','status']
    list_editable = ['status']

admin.site.register(Curricula,CurriculaAdmin)
admin.site.register(Classroom,ClassroomAdmin)
admin.site.register(ClassroomOrder,ClassroomOrderAdmin)
