from django.shortcuts import render, redirect
from core.forms import VolunteerForm, CustomUserCreationForm as UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import login_required
from core.models import Volunteer


# Create your views here.
def register(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('dog_list')
    else:
        form = UserCreationForm()

    return render(request, "core/register.html", {"form": form})


@login_required
def volunteer_application(request):
    try:
        current_volunteer = request.user.volunteer
        form_title = "Update volunteer record"
        button_title = "Save updates"
    except Volunteer.DoesNotExist:
        current_volunteer = Volunteer()
        form_title = "Sign up to be a volunteer"
        button_title = "Submit application"

    if request.POST:
        form = VolunteerForm(request.POST, instance=current_volunteer)
        if form.is_valid():
            volunteer = form.save(commit=False)
            volunteer.user = request.user
            volunteer.save()
            return redirect('dog_list')
    else:
        form = VolunteerForm(instance=current_volunteer)

    return render(request, "core/volunteer_application.html", {
        "form": form,
        "form_title": form_title,
        "button_title": button_title,
    })
