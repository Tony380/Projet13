from django.shortcuts import render, redirect
from .models import Department, Region, Favorite
from .wiki import Wiki
from django.contrib import messages
from .communes import communes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
import os

api_key = os.environ.get('API_KEY')


def paginate(request, args, element_per_page):
    """ Paginate function """
    paginator = Paginator(args, element_per_page)
    page_number = request.GET.get('page', 1)

    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return page_obj


def france(request):
    """ Metropole page """
    regions = Region.objects.all()
    title = 'France métropolitaine'
    wiki_page = Wiki('France métropolitaine').search()
    wiki_summary = wiki_page['page']
    wiki_url = wiki_page['url']
    context = {'regions': regions,
               'wiki_summary': wiki_summary,
               'wiki_url': wiki_url,
               'title': title}
    return render(request, 'france.html', context)


def region(request, region_id):
    """ Regions page """
    depts = Department.objects.filter(region=region_id)
    region = Region.objects.get(id=region_id)
    title = region.name + ' région'
    wiki_page = Wiki(title).search()
    wiki_summary = wiki_page['page']
    wiki_url = wiki_page['url']

    context = {'depts': depts,
               'region': region,
               'wiki_summary': wiki_summary,
               'wiki_url': wiki_url,
               'title': title}
    return render(request, 'region.html', context)


def department(request, department_id):
    """Department page"""
    department = Department.objects.get(id=department_id)
    dept_class = department.class_name
    coms = []
    for key in communes:
        if communes[key] == dept_class[-2:]:
            coms.append(key)
    coms.sort()
    title = department.name + ' département'
    wiki_page = Wiki(title).search()
    wiki_summary = wiki_page['page']
    wiki_url = wiki_page['url']
    if department.name == 'Ville de Paris':
        google_url = f'https://maps.googleapis.com/maps/api/staticmap?center={department.name}' \
                     f',FR&zoom=12&size=650x650&key={api_key}'
    else:
        google_url = f'https://maps.googleapis.com/maps/api/staticmap?center={department.name}' \
                     f',FR&zoom=9&size=650x650&key={api_key}'
    context = {'department': department,
               'page_obj': paginate(request, coms, 102),
               'wiki_summary': wiki_summary,
               'wiki_url': wiki_url,
               'google_url': google_url,
               'title': title}
    return render(request, 'department.html', context)


def commune(request, com):
    """Commune page"""
    title = com + ' commune'
    wiki_page = Wiki(title).search()
    wiki_summary = wiki_page['page']
    wiki_url = wiki_page['url']
    if com == 'Paris':
        google_url = f'https://maps.googleapis.com/maps/api/staticmap?center={com}' \
                     f',FR&zoom=12&size=600x600&key={api_key}'
    else:
        google_url = f'https://maps.googleapis.com/maps/api/staticmap?center={com}' \
                     f',FR&zoom=14&size=600x600&key={api_key}'

    context = {'wiki_summary': wiki_summary,
               'wiki_url': wiki_url,
               'google_url': google_url,
               'com': com,
               'title': title}
    return render(request, 'commune.html', context)


@login_required
def save(request, title):
    """ Saves Wikipedia articles in favorites """
    user = request.user
    try:
        fav = Favorite.objects.filter(title=title,
                                      user_id=user.id)
        if not fav:
            Favorite.objects.create(title=title,
                                    user_id=user.id)
            messages.success(request, 'Article sauvegardé avec succès')
        else:
            messages.success(request, 'Cet article est déjà sauvegardé')

    finally:
        return redirect(request.META.get('HTTP_REFERER'))


@login_required
def del_favorite(request, title):
    """ Delete articles in favorites """
    user = request.user
    favorite = Favorite.objects.get(title=title, user_id=user.id)
    favorite.delete()
    messages.success(request, 'Le favori à été supprimé avec succès')
    return redirect(request.META.get('HTTP_REFERER'))
