from django.shortcuts import render, redirect
from datetime import datetime

from .models import Notice


def index_view(request):
    notices = Notice.objects.all().order_by('created').reverse()
    today = datetime.today()
    return render(request, 'app_notice/index.html', {'notice_list': notices, 'today': today})


def new_view(request):
    if request.method == "POST":
        notice = Notice()
        notice.author = request.user
        notice.content = request.POST.get('content')
        notice.save()
        return redirect('app_notice:index')
    return render(request, 'app_notice/new.html')


def delete(request, notice_id):
    notices = Notice.objects.get(pk=notice_id)
    notices.delete()
    return redirect('app_notice:index')

