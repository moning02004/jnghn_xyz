from django.shortcuts import render


def index_view(request):
    return render(request, 'app_freetalk/index.html')


def new_view(request):
    return render(request, 'app_freetalk/new.html')