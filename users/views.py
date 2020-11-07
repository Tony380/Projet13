from django.shortcuts import render, redirect
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, PasswordChangeView


def register(request):
    """ User registration function """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request,
                             'Bienvenu! Votre compte a été créé avec succès ! '
                             'Vous êtes maintenant connecté')
            login(request, user)
            return redirect('index')
        else:
            form = RegisterForm(request.POST)
            return render(request, 'register.html', {'form': form})

    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    """ User's profile page with data changes possibilty"""
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Informations mis à jour avec succès !')
            return redirect('users:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'profile.html', context)


class LoginFormView(SuccessMessageMixin, LoginView):
    """ Add a welcome message when user logs in """
    success_message = "Bienvenu! Vous êtes maintenant connecté"


class PasswordView(SuccessMessageMixin, PasswordChangeView):
    """ Add a success message when user modifies his password """
    success_message = "Votre mot de passe a été modifié avec succès !"


@login_required
def logout_view(request):
    """ User logout function """
    logout(request)
    messages.success(request, 'Au revoir! Vous êtes maintenant déconnecté')
    return redirect('index')


@login_required
def del_user(request):
    """ User account delete function """
    user = request.user
    logout(request)
    user.delete()
    messages.success(request, "Votre profil a été supprimé avec succès !")
    return redirect('index')
