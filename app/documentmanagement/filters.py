import django_filters
from django.db.models import Q
from .models import Document, DocumentState


class DocumentFilter(django_filters.FilterSet):
    document_type = django_filters.NumberFilter(field_name='document_type__id')
    document_type_description = django_filters.CharFilter(field_name='document_type__description', lookup_expr='icontains')
    
    code = django_filters.CharFilter(lookup_expr='icontains')
    document_name = django_filters.CharFilter(lookup_expr='icontains')
    
    created_after = django_filters.DateFilter(field_name='creation_date', lookup_expr='gte')
    created_before = django_filters.DateFilter(field_name='creation_date', lookup_expr='lte')
    
    revised_after = django_filters.DateFilter(field_name='revision_date', lookup_expr='gte')
    revised_before = django_filters.DateFilter(field_name='revision_date', lookup_expr='lte')
    
    document_state = django_filters.ChoiceFilter(choices=DocumentState.choices)
    
    retention_after = django_filters.DateFilter(field_name='retention_period', lookup_expr='gte')
    retention_before = django_filters.DateFilter(field_name='retention_period', lookup_expr='lte')
    
    created_by = django_filters.NumberFilter(field_name='created_by__id')
    
    search = django_filters.CharFilter(method='filter_search')
    
    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(code__icontains=value) |
            Q(document_name__icontains=value) |
            Q(observation__icontains=value) |
            Q(document_type__description__icontains=value)
        )
    
    class Meta:
        model = Document
        fields = [
            'document_type', 'document_type_description', 'code', 'document_name',
            'created_after', 'created_before', 'revised_after', 'revised_before',
            'document_state', 'retention_after', 'retention_before', 'created_by', 'search'
        ]