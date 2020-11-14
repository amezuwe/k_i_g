from django.contrib import admin
from .models import Investment
from django.contrib.auth.models import User

from django.urls import path
from django.db import models
from django.shortcuts import render


# admin.site.site_header = ""
# admin.site.site_title = ""
# admin.site.index_title = ""


class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'investor', 'date', 'notes')
    list_filter = ('investor',)
    search_fields = ['investor']



admin.site.register(Investment, InvestmentAdmin)



# my dummy model
class DummyModel(models.Model):

    class Meta:
        verbose_name_plural = 'Dummy Model'
        app_label = 'main'

def my_custom_view(request):
    # return HttpResponse('Admin Custom View')
    all_investments = Investment.objects.all()
    investors = User.objects.all()
    users_and_investments = {}
    total_investments = 0
    no_of_investors = 0
    for user in User.objects.all():
        user_investments = user.investments.all()
        user_total_investments = 0
        if user_investments:
            for obj in user_investments:
                user_total_investments += obj.amount

        users_and_investments[user.username] = user_total_investments
        total_investments += user_total_investments
        no_of_investors += 1

    context = {
        'users_and_investments': users_and_investments,
    'total_investments': total_investments,
    'no_of_investors': no_of_investors
    }
    return render(request, 'my_custom_view.html', context)

class DummyModelAdmin(admin.ModelAdmin):
    model = DummyModel

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('my_admin_path/', my_custom_view, name=view_name),
        ]
        
admin.site.register(DummyModel, DummyModelAdmin)