from django.shortcuts import render
from events.models import Event


# Create your views here.
def all_events(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events/index.html', {'events': events})
