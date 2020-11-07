from django.shortcuts import render
from .models import Department, Region
from .wiki import Wiki
from .communes import communes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    wiki_page = Wiki('France métropolitaine').search()
    wiki_summary = wiki_page['page']
    wiki_url = wiki_page['url']
    context = {'regions': regions,
               'wiki_summary': wiki_summary,
               'wiki_url': wiki_url}
    return render(request, 'france.html', context)


def region(request, region_id):
    """ Regions page """
    depts = Department.objects.filter(region=region_id)
    region = Region.objects.get(id=region_id)
    wiki_page = Wiki(region.name + ' région').search()
    wiki_summary = wiki_page['page']
    wiki_url = wiki_page['url']

    context = {'depts': depts,
               'region': region,
               'wiki_summary': wiki_summary,
               'wiki_url': wiki_url}
    return render(request, 'region.html', context)


def department(request, department_id):
    department = Department.objects.get(id=department_id)
    dept_class = department.class_name
    coms = []
    for key in communes:
        if communes[key] == dept_class[-2:]:
            coms.append(key)
    coms.sort()
    wiki_page = Wiki(department.name + ' département').search()
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
               'google_url': google_url}
    return render(request, 'department.html', context)


def commune(request, com):
    wiki_page = Wiki(com + ' commune').search()
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
               'com': com}
    return render(request, 'commune.html', context)
