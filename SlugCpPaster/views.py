from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Slug
from django.utils import timezone
from datetime import datetime
import random as rd

def form_viewer(request):
    return render(request, 'form.html')

def slug_creator(request):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    if request.method == 'POST':
        input_slug = request.POST.get('slug')
        input_content = request.POST.get('content')
        input_slug = input_slug if input_slug else ''.join(rd.choices(letters, k=4))
        print(input_slug)
        # Parse expiry_time safely
        input_time_str = request.POST.get('expiry_time')
        try:
            input_time = datetime.strptime(input_time_str, '%Y-%m-%dT%H:%M')
            input_time = timezone.make_aware(input_time)
        except (ValueError, TypeError):
            return HttpResponse("Invalid datetime format", status=400)

        time_now = timezone.now()

        if time_now > input_time:
            return HttpResponse("Expiry date cannot be in the past", status=400)

        obj, created = Slug.objects.update_or_create(
            slug=input_slug,
            defaults={
                'slug_content': input_content,
                'time_limit': input_time,
                'created_time': time_now
            }
        )

        return redirect(f'/{input_slug}')
    return HttpResponse("Invalid request", status=400)

from django.shortcuts import render
from django.utils import timezone
from django.http import Http404
from .models import Slug

def show_content(request, input_slug):
    time_now = timezone.now()
    try:
        obj = Slug.objects.get(slug=input_slug)
        if time_now <= obj.time_limit:
            time_left = obj.time_limit - time_now
            context = {
                'slug': obj.slug,
                'content': obj.slug_content,
                'time_left_days': time_left.days,
                'hours': time_left.seconds // 3600,
                'minutes': (time_left.seconds // 60) % 60,
                'seconds': time_left.seconds % 60
            }
            return render(request, 'output.html', context)
        else:
            return render(request, 'output.html', {'expired': True})
    except Slug.DoesNotExist:
        raise Http404("Slug not found")
