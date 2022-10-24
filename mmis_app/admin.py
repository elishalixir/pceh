from django.contrib import admin
from .models import User, MercuryAddedProducts, EnergyConsumptionAndFuelProduction, Cement, EnvironmentAndHealth,\
    ASGMining


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'gender']
    list_per_page = 10
    search_fields = ['username', 'gender']


class MercuryAddedProductsAdmin(admin.ModelAdmin):
    list_display = ['author', 'mercury_compound', 'item', 'imported', 'consumption_or_production',
                    'year',  'created_at']
    list_per_page = 10
    search_fields = ['mercury_compound', 'item', 'imported', 'consumption_or_production',
                     'year', 'created_at']


class EnergyConsumptionAndFuelProductionAdmin(admin.ModelAdmin):
    list_display = ['author', 'energy_fuel', 'imported', 'consumption_or_production',
                    'year', 'created_at']
    list_per_page = 10
    search_fields = ['energy_fuel', 'imported', 'consumption_or_production',
                     'year', 'created_at']


class CementAdmin(admin.ModelAdmin):
    list_display = ['author', 'operation_cover', 'yes', 'consumption_or_production',
                    'year', 'created_at']
    list_per_page = 10
    search_fields = ['energy_fuel', 'yes', 'consumption_or_production',
                     'year', 'created_at']


admin.site.register(User, UserAdmin)
admin.site.register(MercuryAddedProducts, MercuryAddedProductsAdmin)
admin.site.register(EnergyConsumptionAndFuelProduction, EnergyConsumptionAndFuelProductionAdmin)
admin.site.register(Cement, CementAdmin)
admin.site.register(EnvironmentAndHealth)
admin.site.register(ASGMining)
