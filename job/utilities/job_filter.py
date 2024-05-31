import django_filters
from ..models import Jobs
import ast

class JobFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(method='filter_by_category')
    timing = django_filters.CharFilter(method='filter_by_timing')
    class Meta:
        model = Jobs
        fields = {
            'min_salary': ['exact', 'gte', 'lte'],
            'level': ['exact'],
            'location': ['exact'],
            'timing': ['exact'],
            'salary_mode': ['exact'],
            'company__location': ['icontains']
        }

    def filter_by_category(self, queryset, name, value):
       
        categories = ast.literal_eval(value)
        queryset = queryset.filter(category__in=categories)
        return queryset
    
    
    def filter_by_timing(self, queryset, name, value):
        print(value)
        timing_list = ast.literal_eval(value)
        queryset = queryset.filter(timing__in=timing_list)
        return queryset
