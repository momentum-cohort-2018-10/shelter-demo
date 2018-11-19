from django.shortcuts import render
from pets.models import Dog
from pets.forms import SearchForm, AdoptionForm

# Create your views here.


def index(request):
    if request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            dogs = Dog.objects.all()
            if data['age']:
                dogs = dogs.filter(age=data['age'])
            if data['size']:
                dogs = dogs.filter(size__in=data['size'])
            if data['good_with_kids']:
                dogs = dogs.filter(good_with_kids=True)
            if data['good_with_dogs']:
                dogs = dogs.filter(good_with_dogs=True)
            if data['good_with_cats']:
                dogs = dogs.filter(good_with_cats=True)

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
