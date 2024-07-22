from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from network.models import Product, Network


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Product model settings in admin panel"""
    list_display = ('name', 'model', 'release_date')
    search_fields = ('name', 'model')
    ordering = ('name',)
    list_filter = ('release_date',)


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    """Network model settings in admin panel"""
    list_display = (
        'name', 'email', 'country', 'city', 'type', 'level', 'debt_to_supplier', 'created_at', 'supplier_link')
    list_filter = ('city', 'type', 'level')
    search_fields = ('name', 'email', 'country', 'city', 'street', 'house_number')
    ordering = ('level', 'name')

    # function for creating a link to supplier
    def supplier_link(self, obj):
        if obj.supplier:
            url = reverse('admin:network_network_change', args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return '-'

    # here we name column of links in admin
    supplier_link.short_description = 'Supplier'

    # this will clear all chosen network's debt updated to 0 in admin
    def clear_debt(self, request, queryset):
        count = queryset.update(debt_to_supplier=0)
        self.message_user(request, f'{count} networks had their debt cleared.')

    # message after using action clear_debt
    clear_debt.short_description = "Clear debt for selected networks"

    # adding clear_debt in admin to using
    actions = [clear_debt]
