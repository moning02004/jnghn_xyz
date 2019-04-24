from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'app_portfolio/index.html')


def detail_view(request, pk):
    return render(request, 'error.html')


def new_view(request):
    return render(request, 'error.html')


def edit_view(request, pk):
    return render(request, 'error.html')


def delete(request, pk):
    return render(request, 'error.html')
