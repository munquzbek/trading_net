import django_filters

from network.models import Network


class NetworkFilter(django_filters.FilterSet):
    """filter by country in api example 'http://127.0.0.1:8000/network/?country=usa'"""
    country = django_filters.CharFilter(field_name='country', lookup_expr='icontains', label='country')

    class Meta:
        model = Network
        fields = ['country']