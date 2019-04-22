from django.shortcuts import render, redirect

from .models import FreeTalk, CommentFree


def index_view(request):
    freetalk_list = FreeTalk.objects.all().order_by('created').reverse()
    return render(request, 'app_freetalk/index.html', {'freetalk_list': freetalk_list})


def detail_view(request, pk):
    try:
        freetalk = FreeTalk.objects.get(pk=pk)
        active = ['active', '']
        if request.method == "POST":
            comment = CommentFree()
            comment.freetalk = freetalk
            comment.author = request.user
            comment.content = request.POST.get('content')
            comment.save()
            active = ['', 'active']
        return render(request, 'app_freetalk/detail.html', {'freetalk': freetalk, 'content': active[0], 'comment': active[1]})
    except:
        return render(request, 'error.html')


def edit_view(request, pk):
    try:
        freetalk = FreeTalk.objects.get(pk=pk)
        if request.method == "POST":
            freetalk.author = request.user
            freetalk.title = request.POST.get('title')
            freetalk.content = request.POST.get('content')
            freetalk.save()
            return redirect('app_freetalk:index')
        return render(request, 'app_freetalk/edit.html', {'freetalk': freetalk})
    except:
        return render(request, 'error.html')


def new_view(request):
    if not request.user.is_authenticated: return render(request, 'error.html')
    if request.method == "POST":
        freetalk = FreeTalk()
        freetalk.author = request.user
        freetalk.title = request.POST.get('title')
        freetalk.content = request.POST.get('content')
        freetalk.save()
        return redirect('app_freetalk:index')
    return render(request, 'app_freetalk/new.html')


def delete(request, pk):
    if request.user.is_superuser: return render(request, 'error.html')
    try:
        FreeTalk.objects.get(pk= pk).delete()
        return redirect('app_freetalk:index')
    except FreeTalk.DoesNotExist:
        return render(request, 'error.html')
