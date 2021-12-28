import django_filters
from course.models import Classroom,ClassroomOrder
 
 
class ClassroomFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(field_name='room_number', lookup_expr='icontains')
 
 
    class Meta:
        model = Classroom
        fields = ()