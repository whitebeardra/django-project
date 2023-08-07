from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.utils import timezone
from .models import Post, shopping_item


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context = {"dataset": Post.objects.all()}
    return render(request, 'polls/img.html', {'posts': posts}, context)
def shoppy(request):
    context = {"dataset": shopping_item.objects.all()}

    return render(request, "polls/img.html", context)

def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()

    context = {"dataset": hotel_image_view.objects.all()}
    return render(request, 'polls/img.html', {'form': form}, context)


def success(request):
    return HttpResponse('successfully uploaded')