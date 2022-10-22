from django.contrib import admin
from .models import User, MercuryAddedProducts, EnergyConsumptionAndFuelProduction, Cement


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'sector', 'gender']
    list_per_page = 10
    search_fields = ['username', 'role', 'sector', 'gender']


class MercuryAddedProductsAdmin(admin.ModelAdmin):
    list_display = ['mercury_compound', 'item', 'imported', 'consumption_or_production',
                    'year', 'note', 'created_at']
    list_per_page = 10
    search_fields = ['mercury_compound', 'item', 'imported', 'consumption_or_production',
                     'year', 'created_at']


class EnergyConsumptionAndFuelProductionAdmin(admin.ModelAdmin):
    list_display = ['energy_fuel', 'imported', 'consumption_or_production',
                    'year', 'note', 'created_at']
    list_per_page = 10
    search_fields = ['energy_fuel', 'imported', 'consumption_or_production',
                     'year', 'created_at']


# class CementAdmin(admin.ModelAdmin):
#     list_display = ['operation_cover', 'yes', 'consumption_or_production',
#                     'year', 'note', 'created_at']
#     list_per_page = 10
#     search_fields = ['energy_fuel', 'yes', 'consumption_or_production',
#                      'year', 'created_at']
#

admin.site.register(User, UserAdmin)
admin.site.register(MercuryAddedProducts, MercuryAddedProductsAdmin)
admin.site.register(EnergyConsumptionAndFuelProduction, EnergyConsumptionAndFuelProductionAdmin)
# admin.site.register(Cement, CementAdmin)
