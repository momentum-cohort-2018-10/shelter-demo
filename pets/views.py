from django.shortcuts import render
from pets.models import Dog
from pets.forms import SearchForm, AdoptionForm

# Create your views here.


def index(request):
    if request.GET:
        form = SearchForm(request.GET)
        dogs = form.search()
    else:
        form = SearchForm()
        dogs = Dog.objects.all()

    response = render(request, 'pets/index.html', {
        "shelter_name": "Lazy River Shelter",
        "dogs": dogs,
        "search_form": form,
    })
    return response


def dog(request, dog_id):
    dog = Dog.objects.get(pk=dog_id)
    adoption_form = AdoptionForm(initial={"dog": dog})
    response = render(
        request, 'pets/dog.html', {
            "shelter_name": "Lazy River Shelter",
            "dog": dog,
            "adoption_form": adoption_form,
        })
    return response


def create_application(request, dog_id):
    adoption_form = AdoptionForm(request.POST)
    if adoption_form.is_valid():
        application = adoption_form.save()
        return render(request, 'pets/application_received.html', {
            "shelter_name": "Lazy River Shelter",
            "application": application
        })

    dog = Dog.objects.get(pk=dog_id)
    return render(
        request, 'pets/dog.html', {
            "shelter_name": "Lazy River Shelter",
            "dog": dog,
            "adoption_form": adoption_form,
        })


def contact(request):
    return render(request, "pets/contact.html", {
        "shelter_name": "Lazy River Shelter",
    })
