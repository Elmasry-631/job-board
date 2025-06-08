import django_filters
from .models import Job


class JobFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fildes = '__all__'
        exclude = ['published_at', 'image','salary', 'description', 'slug', 'owner',]
        # 'title', 'description', 'slug', 'owner' are excluded from the filter
        