from django.shortcuts import render, get_object_or_404
from .models import Event, Category, OurActivity


def Home(request):
    cat = Category.objects.all()
    return render(request, 'index.html', {'cat': cat})


def event_list(request):
    events = Event.objects.all().order_by('-date')
    return render(request, 'events.html', {'events': events})


def event_detail(request, uid):
    event = get_object_or_404(Event, uid=uid)
    return render(request, 'event_detail.html', {'event': event})


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    activities = OurActivity.objects.filter(category=category)
    return render(request, 'recents.html', {'category': category, 'activities': activities})


def volunteer(request):
    return render(request, 'volunteer.html')
