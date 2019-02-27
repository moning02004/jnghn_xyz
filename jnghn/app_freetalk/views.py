from django.shortcuts import render, redirect

from .models import FreeTalk


def index_view(request):
    freetalk_list = FreeTalk.objects.all().order_by('created').reverse()
    return render(request, 'app_freetalk/index.html', {'freetalk_list': freetalk_list})


def detail_view(request, pk):
    freetalk = FreeTalk.objects.get(pk=pk)
    return render(request, 'app_freetalk/detail.html', {'freetalk': freetalk})


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