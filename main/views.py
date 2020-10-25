from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:login')
def home(request):
    return redirect('main:investment_list')


@login_required(login_url='accounts:login')
def investment_list(request):
    current_user = request.user
    user_investments = current_user.investments.all().order_by('date')
    total_investments = 0
    if user_investments:
        for obj in user_investments:
            total_investments += obj.amount
    context = {
        'investments': user_investments,
        'current_user': current_user,
        'total_investments': total_investments
    }
    return render(request, 'main/list.html', context)
