from django.contrib import admin
from .models import Investment

admin.site.site_header = ""
admin.site.site_title = ""
admin.site.index_title = ""


class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'investor', 'date', 'notes')
    list_filter = ('investor',)
    search_fields = ['investor']


admin.site.register(Investment, InvestmentAdmin)