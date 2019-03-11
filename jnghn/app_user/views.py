from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from app_notice.models import Notice
from app_plan.models import Plan, HeartPlan
from app_archive.models import Archive

def login_view(request):
    if request.user.is_authenticated: return render(request, 'error.html')
    if request.method == "POST":
        try:
            user = User.objects.get(username=request.POST.get('username'))
            if user.check_password(request.POST.get('password')):
                auth.login(request, user)
                if request.session.get('last'):
                    last = request.session['last']
                    del request.session['last']
                    return redirect(str(last) + ':index')
                return redirect('app_main:index')
        except User.DoesNotExist:
            pass
        return render(request, 'app_user/login.html', {'message': "Username or Password is not correct"})
    return render(request, 'app_user/login.html')


def register_view(request):
    if request.user.is_authenticated: return render(request, 'error.html')
    if request.method == "POST":
        user = User()
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('name')

        if request.POST.get('user_check') == "user_check":
            try:
                User.objects.get(username=request.POST.get('username'))
                message = "This username is already registered"
            except User.DoesNotExist:
                message = "This username can use this username"
            return render(request, 'app_user/register.html', {'userObject': user, 'message': message})
        user.set_password(request.POST.getlist('password')[0])
        user.save()
        return redirect('app_user:login')
    return render(request, 'app_user/register.html')


def logout(request):
    if not request.user.is_authenticated: return render(request, 'error.html')
    auth.logout(request)
    return redirect('app_user:login')


def leave(request, username):
    if not request.user.is_authenticated: return render(request, 'error.html')
    if username == request.user.username:
        user = User.objects.get(username=username).delete()
        return redirect('app_main:index')
    return render(request, 'error.html')


def profile_view(request):
    plan_list = Plan.objects.all().filter(author=request.user)
    archive_list = Archive.objects.all().filter(author=request.user)
    context = {'plan_list': plan_list, 'archive_list': archive_list}

    return render(request, 'app_user/profile.html', context)



def edit_view(request):
    if not request.user.is_authenticated: return render(request, 'error.html')
    try:
        user = User.objects.get(username=request.user)
        if request.method == "POST":
            if user.check_password(request.POST.get('current_password')):
                user.first_name = request.POST.get('name')
                user.email = request.POST.get('email')
                if request.POST.getlist('password')[0] != "":
                    if request.POST.getlist('password')[0] == request.POST.getlist('password')[1]:
                        user.set_password(request.POST.getlist('password')[0])
                    else:
                        return render(request, 'app_user/edit.html',
                                      {'object': user, 'new_password_message': 'Type the new password correctly!'})
                user.save()
                auth.login(request, user)
                return redirect('app_user:profile')
            return render(request, 'app_user/edit.html',
                          {'object': user, 'current_password_message': 'Type the current password correctly!'})

        return render(request, 'app_user/edit.html', {'object': user})
    except User.DoesNotExist:
        return render(request, 'error.html')


def find_view(request):
    if request.user.is_authenticated: return render(request, 'error.html')
    if request.method == "POST":
        if request.POST.get('domain') == "other":
            email = request.POST.get('email') + "@" + request.POST.get('domain')
        email = request.POST.get('email')+request.POST.get('domain')
        try:
            user = User.objects.get(email=email)
            if user.first_name != request.POST.get('name'):
                return render(request, 'app_user/find/find.html', {'message': 'Not Exist matched name & email'})
            return render(request, 'app_user/find/reset.html', {'object': user})
        except User.DoesNotExist:
            return render(request, 'app_user/find/find.html', {'message': 'Not Exist matched name & email'})
    return render(request, 'app_user/find/find.html')


def reset_view(request):
    if request.user.is_authenticated: return render(request, 'error.html')
    if request.method == "POST":
        user = User.objects.get(username=request.POST.get('username'))
        if request.POST.getlist('password')[0] != "" and (request.POST.getlist('password')[0] == request.POST.getlist('password')[1]):
            user.set_password(request.POST.getlist('password')[0])
            user.save()
    return redirect('app_user:login')
