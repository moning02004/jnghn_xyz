from django.shortcuts import render, redirect

from .models import Material, Attachment, CommentMaterial


def index_view(request):
    material_list = Material.objects.all().order_by('created').reverse()
    return render(request, 'app_material/index.html', {'material_list':material_list})


def detail_view(request, pk):
    try:
        material = Material.objects.get(pk=pk)
        active = ['active', '']
        if request.method == "POST":
            comment = CommentMaterial()
            comment.material = material
            comment.author = request.user
            comment.content = request.POST.get('comment')
            comment.save()
            active = ['', 'active']
        else:
            material.view += 1
            material.save()
        return render(request, 'app_material/detail.html', {'material': material, 'content': active[0], 'comment': active[1]})
    except Material.DoesNotExist:
        return render(request, 'error.html')


def new_view(request):
    if not request.user.is_authenticated: return render(request, 'error.html')
    if request.method == "POST":
        material = Material()
        material.author = request.user
        material.title = request.POST.get('title')
        material.content = request.POST.get('content')
        material.save()

        for file in request.FILES.getlist('attachment'):
            attachment = Attachment()
            attachment.material = material
            attachment.file = file
            attachment.save()
        return redirect('app_material:index')
    return render(request, 'app_material/new.html')


def edit_view(request, pk):
    if not request.user.is_authenticated: return render(request, 'error.html')
    try:
        material = Material.objects.get(pk=pk)
        if request.method == "POST":
            material.title = request.POST.get('title')
            material.content = request.POST.get('content')
            material.save()
            
            for file in request.FILES.getlist('attachment'):
                files = Attachment()
                files.material = material
                files.file = file
                files.save()
            return redirect('app_material:index', 1)
        return render(request, 'app_material/edit.html', {'material': material})
    except Material.DoesNotExist:
        return render(request, 'error.html')


def delete(request, pk):
    if not request.user.is_authenticated: return render(request, 'error.html')
    try:
        material = Material.objects.get(pk=pk)
        if material.author == request.user or request.user.is_superuser or request.user.last_name == "Administrator":
            for attachment in material.attachment_set.all() :
                attachment.file.delete()
            material.delete()
            return redirect('app_material:index')
    except Material.DoesNotExist: pass
    return render(request, 'error.html')


def delete_file(request, pk, file_id):
    file = Material.objects.get(pk=pk).attachment_set.get(pk=file_id)
    file.file.delete()
    file.delete()
    return redirect('app_material:edit', pk)