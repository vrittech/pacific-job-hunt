import django_filters
from ..models import Jobs
import ast

class JobFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(method='filter_by_category')
    timing = django_filters.CharFilter(method='filter_by_timing')
    location = django_filters.CharFilter(method='filter_by_location')
    class Meta:
        model = Jobs
        fields = {
            'min_salary': ['exact', 'gte', 'lte'],
            'level': ['exact'],
            'salary_mode': ['exact'],
            'company__location': ['icontains']
        }

    def filter_by_category(self, queryset, name, value):
       
        categories = self.request.GET.getlist('category')
        queryset = queryset.filter(category_id__in=categories)
        return queryset
    

    def filter_by_location(self, queryset, name, value):
        locations = self.request.GET.getlist('location')
        if locations:
            queryset = queryset.filter(location__in=locations)
        return queryset
    
    
    def filter_by_timing(self, queryset, name, value):
        
        timing_list = self.request.GET.getlist('timing')
        queryset = queryset.filter(timing__in=timing_list)
        return queryset
