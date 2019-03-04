from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from app_plan.models import Plan
from .models import Review, Image, Cost, HeartReview, CommentReview


def index_view(request):
    if not request.user.is_authenticated: return render(request, 'error.html')
    review_list = Review.objects.all().filter(author=request.user).order_by('created').reverse()
    return render(request, 'app_review/index.html', {'review_list': review_list})


def detail_view(request, review_id):
    try:
        review = Review.objects.get(pk=review_id)
        active = ''
        if request.method == "POST":
            if request.POST.get('button') == "heart":
                try:
                    heart = HeartReview.objects.get(author=request.user, review=review)
                    heart.delete()
                except HeartReview.DoesNotExist:
                    heart = HeartReview()
                    heart.review = review
                    heart.author = request.user
                    heart.save()
            elif request.POST.get('button') == "comment":
                comment = CommentReview()
                comment.review = review
                comment.author = request.user
                comment.content = request.POST.get('comment_text')
                comment.save()
                active = 'active'
        else:
            review.view += 1
            review.save()

        color = "red" if request.user.is_authenticated and HeartReview.objects.filter(review=review, author=request.user).exists() else "white"
        return render(request, 'app_review/detail.html', {'review': review, 'color': color, 'comment': active})
    except Review.DoesNotExist:
        return render(request, 'error.html')


def new_view(request, plan_id):
    plan = None
    if not request.user.is_authenticated: return render(request, 'error.html')
    try:
        plan = Plan.objects.get(pk=plan_id)
        review = Review.objects.get(plan=plan)
        return redirect('app_review:detail', review.id)
    except Review.DoesNotExist:
        pass
    if request.method == "POST":
        review = Review()
        review.plan = plan
        review.author = request.user
        review.title = request.POST.get('title')
        review.content = request.POST.get('content')
        review.save()

        for image in request.FILES.getlist('image'):
            images = Image()
            images.review = review
            images.image_file = image
            images.save()

        for cost_content, cost in zip(request.POST.getlist('cost_content'), request.POST.getlist('cost')):
            if cost_content == '': continue
            costs = Cost()
            costs.review = review
            costs.cost_content = cost_content
            costs.cost = int(cost)
            costs.save()
        return redirect('app_review:index')
    return render(request, 'app_review/new.html', {'plan': plan})


def edit_view(request, review_id):
    if not request.user.is_authenticated: return render(request, 'error.html')
    try:
        review = Review.objects.get(pk=review_id)
        if request.method == "POST":
            review.title = request.POST.get('title')
            review.save()

            for image, desc in zip(request.FILES.getlist('files'), request.POST.getlist('desc')):
                content = Content()
                content.review = review
                content.image_file = image
                content.desc = desc
                content.save()
            return redirect('app_review:index')
        return render(request, 'app_review/edit.html', {'review': review})
    except Review.DoesNotExist:
        return render(request, 'error.html')


def delete(request, review_id):
    if not request.user.is_authenticated: return render(request, 'error.html')
    try:
        review = Review.objects.get(pk=review_id)
        if review.author == request.user or \
                request.user.is_superuser or request.user.last_name == "Administrator":
            for content in review.content_set.all():
                content.image_file.delete()
            review.delete()
        return redirect('app_review:index', 1)
    except Review.DoesNotExist:
        return render(request, 'error.html')


def delete_content(request, review_id, file_id):
    content = Review.objects.get(pk=review_id).content_set.get(pk=file_id)
    content.image_file.delete()
    content.delete()
    return redirect('app_review:edit', review_id)
