from django.shortcuts import render, redirect
from .models import Investment
from django.contrib.auth.decorators import login_required



@login_required(login_url='accounts:login')
def home(request):
    # context = {}
    # return render(request, 'base.html', context)
    return redirect('main:investment_list')


@login_required(login_url='accounts:login')
def investment_list(request):
    current_user = request.user 
    user_investments = Investment.objects.filter(investor=current_user).order_by('date')
    context = {
        'investments': user_investments,
        'current_user': current_user
    }
    return render(request, 'main/list.html', context)
