from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from .models import Archive, Attachment, CommentArchive


def index_view(request):
    archive_list = Archive.objects.all().order_by('created').reverse()
    return render(request, 'app_archive/index.html', {'archive_list':archive_list})


def detail_view(request, archive_id):
    try:
        archive = Archive.objects.get(pk=archive_id)
        if request.method == "POST":
            comment = CommentArchive()
            comment.archive = archive
            comment.author = request.user
            comment.content = request.POST.get('comment')
            comment.save()

        else:
            archive.view += 1
            archive.save()
        return render(request, 'app_archive/detail.html', {'archive': archive})
    except Archive.DoesNotExist:
        return render(request, 'error.html')


def new_view(request):
    if not request.user.is_authenticated: return render(request, 'error.html')
    if request.method == "POST":
        archive = Archive()
        archive.author = request.user
        archive.title = request.POST.get('title')
        archive.content = request.POST.get('content')
        archive.save()

        for file in request.FILES.getlist('attachment'):
            attachment = Attachment()
            attachment.archive = archive
            attachment.file = file
            attachment.save()
        return redirect('app_archive:index')
    return render(request, 'app_archive/new.html')


def edit_view(request, archive_id):
    if not request.user.is_authenticated: return render(request, 'error.html')
    try:
        archive = Archive.objects.get(pk=archive_id)
        if request.method == "POST":
            archive.title = request.POST.get('title')
            archive.content = request.POST.get('content')
            archive.save()
            
            for file in request.FILES.getlist('attachment'):
                files = Attachment()
                files.archive = archive
                files.file = file
                files.save()
            return redirect('app_archive:index', 1)
        return render(request, 'app_archive/edit.html', {'archive': archive})
    except Archive.DoesNotExist:
        return render(request, 'error.html')


def delete(request, archive_id):
    if not request.user.is_authenticated: return render(request, 'error.html')
    try:
        archive = Archive.objects.get(pk=archive_id)
        if archive.author == request.user or request.user.is_superuser or request.user.last_name == "Administrator":
            for attachment in archive.attachment_set.all() :
                attachment.file.delete()
            archive.delete()
            return redirect('app_archive:index')
    except Archive.DoesNotExist: pass
    return render(request, 'error.html')


def delete_file(request, archive_id, file_id):
    file = Archive.objects.get(pk=archive_id).attachment_set.get(pk=file_id)
    file.file.delete()
    file.delete()
    return redirect('app_archive:edit', archive_id)