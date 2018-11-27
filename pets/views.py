from django.shortcuts import render, redirect
from pets.models import Dog
from pets.forms import SearchForm, AdoptionForm
from django.contrib import messages

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
        success_msg = f"Your application to adopt {application.dog.name} has been received! We will contact you at {application.email} within 2-3 days."
        messages.add_message(request, messages.SUCCESS, success_msg)

        if application.current_pet_owner and application.dog.needs_no_pets():
            messages.add_message(
                request, messages.ERROR,
                'This dog requires a home with no pets. Your application may be denied.'
            )

        return redirect(to='dog_list')

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
