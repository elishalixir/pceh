from django.contrib import admin
from .models import User, MercuryAddedProducts


# Register your models here.
class MercuryAddedProductsAdmin(admin.ModelAdmin):
    list_display = ['mercury_compound', 'item', 'imported', 'consumption_or_production',
                    'year', 'note', 'created_at']
    list_per_page = 10
    search_fields = ['mercury_compound', 'item', 'imported', 'consumption_or_production',
                     'year', 'created_at']


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'sector', 'gender']
    list_per_page = 10
    search_fields = ['username', 'role', 'sector', 'gender']


admin.site.register( MercuryAddedProducts, MercuryAddedProductsAdmin)
admin.site.register(User, UserAdmin)
