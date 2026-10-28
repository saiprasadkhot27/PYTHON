

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import LoginForm


def login_view(request):

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            messages.success(
                request,
                f"Login successful! Welcome {username}."
            )

            return redirect('success')

    else:
        form = LoginForm()

    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )


def success_view(request):

    return render(
        request,
        'accounts/success.html'
    )