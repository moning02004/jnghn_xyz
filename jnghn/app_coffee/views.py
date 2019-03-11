from django.db.models import Sum
from django.shortcuts import render, redirect
from datetime import datetime

from .models import Account, Beans, Community, CommentCommunity


def beans_index(request):
    beans_list = Beans.objects.all()
    return render(request, 'app_coffee/beans_index.html', {'beans_list': beans_list})


def beans_new(request):
    if not request.user.is_superuser: return render(request, 'error.html')
    if request.method == "POST":
        beans = Beans()
        beans.nation = request.POST.get('nation')
        beans.name = request.POST.get('name')
        beans.content = request.POST.get('desc')
        beans.save()
        return redirect('app_coffee:beans')
    return render(request, 'app_coffee/beans_new.html')


def beans_edit(request, pk):
    try:
        beans = Beans.objects.get(pk=pk)
        if request.method == "POST":
            beans.nation = request.POST.get('nation')
            beans.name = request.POST.get('name')
            beans.content = request.POST.get('desc')
            beans.save()
            return redirect('app_coffee:beans')
        return render(request, 'app_coffee/beans_edit.html', {'beans': beans})
    except:
        return render(request, 'error.html')


def beans_delete(request, pk):
    try:
        beans = Beans.objects.get(pk=pk)
        if request.method == "POST":
            beans.nation = request.POST.get('nation')
            beans.name = request.POST.get('name')
            beans.content = request.POST.get('desc')
            beans.save()
            return redirect('app_coffee:beans')
        return render(request, 'app_coffee/beans_edit.html', {'beans': beans})
    except:
        return render(request, 'error.html')


def community_index(request):
    post_list = Community.objects.all().order_by('created').reverse()
    return render(request, 'app_coffee/community_index.html', {'post_list': post_list})


def community_new(request):
    if not request.user.is_authenticated: return render(request, 'error.html')
    if request.method == "POST":
        post = Community()
        post.author = request.user
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('app_coffee:community')
    return render(request, 'app_coffee/community_new.html')


def community_edit(request, pk):
    try :
        post = Community.objects.get(pk=pk)
        if not request.user.is_authenticated and post.author != request.user: return render(request, 'error.html')
        if request.method == "POST":
            post.author = request.user
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.save()
            return redirect('app_coffee:community_detail', pk)
        return render(request, 'app_coffee/community_edit.html', {'post': post})
    except:
        return render(request, 'error.html')


def community_detail(request, pk):
    try:
        post = Community.objects.get(pk=pk)
        active = ['active', '']
        if request.method == "POST":
            if request.POST.get('button') == "comment":
                comment = CommentCommunity()
                comment.community = post
                comment.author = request.user
                comment.content = request.POST.get('content')
                comment.save()
                active = ['', 'active']
        else:
            post.view += 1
            post.save()
        return render(request, 'app_coffee/community_detail.html', {'post': post, 'content': active[0], 'comment':active[1]})
    except Community.DoesNotExist:
        return render(request, 'error.html')


def community_delete(request, pk):
    try:
        Community.objects.get(pk=pk)
        return redirect('app_coffee:community')
    except Community.DoesNotExist:
        return render(request, 'error.html')


def account_index(request):
    if not request.user.is_authenticated: return render(request, 'error.html')
    account_list = Account.objects.all().filter(author=request.user)
    context = {
        'account_list': account_list,
        'item': str(account_list[0]) + ' and ' + str(len(account_list)-1) + ' others',
        'item_date': str(account_list[0].begin_date) + ' ~ ' + str(account_list.last().begin_date),
        'all_amount': str(account_list.aggregate(amount=Sum('amount')).get('amount')),
        'all_price': str(account_list.aggregate(price=Sum('price')).get('price'))
    }
    return render(request, 'app_coffee/account_index.html', context)


def account_new(request):
    if not request.user.is_authenticated: return render(request, 'error.html')
    if request.method == "POST":
        account = Account()
        account.author = request.user
        account.name = request.POST.get('name')
        account.purchase_site = request.POST.get('site')
        account.begin_date = request.POST.get('date')
        account.amount = request.POST.get('amount')
        account.price = request.POST.get('price')
        account.save()
        return redirect('app_coffee:account')
    return render(request, 'app_coffee/account_new.html')


def account_renew(request, pk):
    try:
        account = Account.objects.get(pk=pk)
        if not request.user.is_authenticated and account.author != request.user: return render(request, 'error.html')
        account.end_date = datetime.now().date()
        account.period = (account.end_date - account.begin_date).days
        print(account.period)
        account.save()
        return redirect('app_coffee:account')
    except:
        return render(request, 'error.html')


def account_delete(request, pk):
    account = Account.objects.get(pk=pk)
    if not request.user.is_authenticated and account.author != request.user: return render(request, 'error.html')
    account.end_date = datetime.now().date()
    account.period = (account.end_date - account.begin_date).days
    print(account.period)
    account.save()
    return redirect('app_coffee:account')
