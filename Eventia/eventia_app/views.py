from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm
from .models import Event
from django.core.paginator import Paginator


def base(request):
    return render(request, 'base.html', {'user': request.user})


def home_page(request):
    return render(request, 'home_page.html')


def events_by_category(request, category):

    events = Event.objects.filter(category=category)
    paginator = Paginator(events, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'eventia_app/events_by_category.html', {
        'page_obj': page_obj,
        'selected_category': category
    })


def all_events(request):
    events = Event.objects.all()
    paginator = Paginator(events, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'eventia_app/all_events.html', {
        'page_obj': page_obj
    })


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'eventia_app/event_detail.html', {
        'event': event
    })


def create_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_events.html')
    else:
        form = EventForm()
    return render(request, 'eventia_app/create_event.html', {'form': form})
