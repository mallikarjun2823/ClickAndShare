from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Slug

def form_viewer(request):
    return render(request, 'form.html')

def slug_creator(request):
    if request.method == 'POST':
        input_slug = request.POST.get('slug')
        input_content = request.POST.get('content')
        input_time = request.POST.get('expiry_time')
        obj, created = Slug.objects.update_or_create(
            slug=input_slug,
            defaults={'slug_content': input_content , 'time_limit': input_time}
        )

        # Redirect to the newly created/updated slug URL
        return redirect(f'/{input_slug}')
    return HttpResponse("Invalid request", status=400)

def show_content(request, input_slug):
    try:
        obj = Slug.objects.get(slug=input_slug)
        return HttpResponse(f"<h1>{obj.slug}</h1><p>{obj.slug_content}</p>")
    except:
        raise Http404("Slug not found")
