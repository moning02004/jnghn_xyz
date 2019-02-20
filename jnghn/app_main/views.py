from django.shortcuts import render

from app_archive.models import Archive
from app_plan.models import Plan
from app_review.models import Review
from app_notice.models import Notice

def index_view(request):
    notice_list = Notice.objects.all().order_by('created').reverse()[:5]
    return render(request, 'app_main/index.html', {'notice_list': notice_list})


def me_view(request):
    return render(request, 'app_main/me.html')


def site_view(request):
    return render(request, 'app_main/site.html')


def search_view(request):
    primary = request.GET.get('search')
    plan_list = Plan.objects.all().filter(title=primary)
    review_list = Review.objects.all().filter(title=primary)
    archive_list = Archive.objects.all().filter(title=primary)
    return render(request, 'app_main/search.html', {'keyword': primary, 'plan': plan_list, 'review': review_list, 'archive': archive_list})
