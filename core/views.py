from django.shortcuts import render, redirect
from core.forms import CustomUserCreationForm as UserCreationForm
from django.contrib.auth import authenticate, login


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
