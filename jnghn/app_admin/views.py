from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def index_view(request):
    if not request.user.is_staff: return render(request, 'error.html')
    user = User.objects.all()
    return render(request, 'app_admin/index.html', {'user_list': user})


def detail_view(request, username):
    if not request.user.is_staff : return render(request, 'error.html')
    try:
        user = User.objects.get(username=username)
        return render(request, 'app_admin/detail.html', {'userObject': user})
    except User.DoesNotExist:
        return render(request, 'error.html')


def edit_view(request, username):
    if not request.user.is_staff: return render(request, 'error.html')
    try:
        user = User.objects.get(username=username)
        if request.method == "POST":
            user.email = request.POST.get('email')
            user.is_staff = request.POST.get('staff')
            user.save()
            return redirect('app_admin:detail', username)
        return render(request, 'app_admin/edit.html', {'userObject': user})
    except User.DoesNotExist:
        return redirect('app_admin:index')


def delete_user(request, username):
    if request.user.is_staff:
        try:
            user = User.objects.get(username=username)
            if user.is_superuser:
                return redirect('app_admin:index')
            for obj in user.gallery_set.all():
                obj.author = None
                obj.save()
            for obj in user.archive_set.all():
                for o in obj.attachment_set.all():
                    o.file.delete()
            user.delete()
            return redirect('app_admin:index')
        except User.DoesNotExist:
            return redirect('app_admin:index')
    return render(request, 'error.html')
