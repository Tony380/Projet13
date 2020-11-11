from django.shortcuts import render, redirect
from .forms import RegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from maps.models import Favorite
from maps.wiki import Wiki


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
    """User's profile page"""
    user = request.user
    favs = Favorite.objects.filter(user_id=user.id)
    favorite = []
    if len(favs) > 0:
        for fav in favs:
            wiki_title = fav.title
            wiki_page = Wiki(fav.title).search()['page']
            wiki_url = Wiki(fav.title).search()['url']
            favorite.append([wiki_title, wiki_page, wiki_url])

    context = {'favorite': favorite}
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


@login_required
def info(request):
    """ User's profile page with data changes possibilty"""
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Informations mis à jour avec succès !')
            return redirect('users:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

        context = {
            'u_form': u_form
        }
        return render(request, 'info.html', context)
