from datetime import datetime
from datetime import timedelta
from django.shortcuts import render, redirect
from django.views import generic

from .models import Plan, Detail, HeartPlan, CommentPlan, Days


def index_view(request):
    if not request.user.is_authenticated: return render(request, 'error.html')
    plan_list = Plan.objects.all().filter(author=request.user).order_by('created').reverse()
    return render(request, 'app_plan/index.html', {'plan_list': plan_list})


def detail_view(request, pk):
    try:
        plan = Plan.objects.get(pk=pk)

        if request.method == "POST":
            # 하트를 클릭할 경우
            if request.POST.get('button') == "heart":
                try:
                    heart = HeartPlan.objects.get(plan=plan, user=request.user)
                    heart.delete()
                except HeartPlan.DoesNotExist:
                    heart = HeartPlan()
                    heart.plan = plan
                    heart.user = request.user
                    heart.save()
            # 댓글 입력할 경우
            elif request.POST.get('button') == "comment":
                comment = CommentPlan()
                comment.plan = plan
                comment.user = request.user
                comment.content = request.POST.get('content')
                comment.save()
            # 완료 버튼 클릭할 경우
            elif request.POST.get('button') == "Finish":
                plan.finish = "Yes"
                plan.save()
            elif request.POST.get('button') == "Not Finish":
                plan.finish = "No"
                plan.save()
                
        else:
            plan.view += 1
            plan.save()
        
        color = "red" if request.user.is_authenticated and HeartPlan.objects.filter(plan=plan, user=request.user).exists() else "white"
        return render(request, 'app_plan/detail.html', {'plan': plan, 'color': color})
    except Plan.DoesNotExist:
        return render(request, 'error.html')


def router_view(request):
    if request.method == "POST":
        return redirect('app_plan:new', request.POST.get('period'))
    return render(request, 'app_plan/router.html')


def new_view(request, period):
    if not request.user.is_authenticated: return render(request, 'error.html')
    if request.method == "POST":
        plan = Plan()
        plan.author = request.user
        plan.title = request.POST.get('title')
        plan.where = request.POST.get('where')
        plan.day_from = request.POST.get('day_from')
        plan.day_to = request.POST.get('day_to')
        plan.period = period
        plan.save()

        for i in range(period):
            days = Days()
            days.plan = plan
            days.save()
            for place, content in zip(request.POST.getlist('place'+str(i)), request.POST.getlist('content'+str(i))):
                print(place)
                detail = Detail()
                detail.days = days
                detail.place = place
                detail.content = content
                detail.save()
        return redirect('app_plan:index')
    return render(request, 'app_plan/new.html', {'period': range(period)})


def edit_view(request, pk):
    if not request.user.is_authenticated: return render(request, 'error.html')
    try:
        plan = Plan.objects.get(pk=pk)
        if request.method == "POST":
            plan.title = request.POST.get('title')
            plan.where = request.POST.get('where')
            plan.when = request.POST.get('when')
            plan.save()

            for detail, place, content in zip(plan.detail_set.all(), request.POST.getlist('e_place'), request.POST.getlist('e_content')):
                detail.place = place
                detail.content = content
                detail.save()

            for place, content in zip(request.POST.getlist('place'), request.POST.getlist('content')):
                if place == "": continue
                detail = Detail()
                detail.plan = plan
                detail.place = place
                detail.content = content
                detail.save()
            return redirect('app_plan:index')
        return render(request, 'app_plan/edit.html', {'plan': plan})
    except Plan.DoesNotExist:
        return render(request, 'error.html')


def delete(request, pk):
    if not request.user.is_authenticated: return render(request, 'error.html')
    try:
        plan = Plan.objects.get(pk=pk)
        if plan.author.username == request.user.username or \
                request.user.is_superuser or request.user.last_name == "Administrator":
            plan.delete()
        return redirect('app_plan:index')
    except Plan.DoesNotExist:
        return render(request, 'error.html')


def delete_plan(request, pk, detail_id):
    if not request.user.is_authenticated: return render(request, 'error.html')
    try:
        detail = Plan.objects.get(pk=pk).detail_set.get(pk=detail_id)
        detail.delete()

    except Plan.DoesNotExist or Detail.DoesNotExist:
        return render(request, 'error.html')
    return redirect('app_plan:edit', pk)


def finish(request, pk):
    if not request.user.is_authenticated: return render(request, 'error.html')
    try:
        plan = Plan.objects.get(pk=pk)
        plan.complete = "Yes"
        plan.save()
    except Plan.DoesNotExist:
        return render(request, 'error.html')
    return redirect('app_plan:detail', pk)
