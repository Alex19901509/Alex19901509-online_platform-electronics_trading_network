from django.contrib import admin
from .models import Supplier, Product, NetworkNode


@admin.action(description='Очистить задолженность')  # Описание для действия
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)  # Обнуляем задолженность для выбранных объектов


class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'city', 'country', 'debt', 'created_at')
    list_filter = ('city', 'country')
    actions = [clear_debt]  # Добавляем действие в админку


admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(NetworkNode, NetworkNodeAdmin)
