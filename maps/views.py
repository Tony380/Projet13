from django.shortcuts import render
from .models import Department, Region
import wikipedia
from maps.communes import communes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os

wikipedia.set_lang("fr")
api_key = os.environ.get('API_KEY')


def paginate(request, args, prods_per_page):
    """ Paginate function """
    paginator = Paginator(args, prods_per_page)
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
    wiki_page = wikipedia.WikipediaPage('France')
    context = {'regions': regions,
               'wiki': wiki_page.section('Localisation, frontières et superficie')[:1168]}
    return render(request, 'france.html', context)


def region(request, region_id):
    """ Regions page """
    depts = Department.objects.filter(region=region_id)
    region = Region.objects.get(id=region_id)

    try:
        wiki_summary = wikipedia.summary(region.name, 4)
        wiki = wikipedia.page(region.name).url

    except wikipedia.DisambiguationError:
        wiki_page = wikipedia.page(region.name + '(région administrative)')
        wiki_summary = wikipedia.page(region.name + '(région administrative)').summary[:878]
        wiki = wiki_page.url

    context = {'depts': depts,
               'region': region,
               'wiki': wiki_summary,
               'wi': wiki}
    return render(request, 'region.html', context)


def department(request, department_id):
    department = Department.objects.get(id=department_id)
    dept_class = department.class_name
    coms = []
    for key in communes:
        if communes[key] == dept_class[-2:]:
            coms.append(key)
    coms.sort()
    wiki_summary = wikipedia.summary(department.name, 4)
    wiki = wikipedia.page(department.name).url
    url = f'https://maps.googleapis.com/maps/api/staticmap?center={department.name}' \
          f',FR&zoom=9&size=650x650&key={api_key}'
    context = {'department': department,
               'page_obj': paginate(request, coms, 102),
               'wiki': wiki_summary,
               'wi': wiki,
               'url': url}
    return render(request, 'department.html', context)


def commune(request, com, dept_id):
    dept = Department.objects.get(id=dept_id)
    wiki_page = wikipedia.page(com + ' ' + dept.name)
    wiki_summary = wikipedia.page(com + ' ' + dept.name).summary
    wiki = wiki_page.url
    url = f'https://maps.googleapis.com/maps/api/staticmap?center={com}' \
          f',FR&zoom=14&size=600x600&key={api_key}'

    context = {'wiki': wiki_summary,
               'wi': wiki,
               'url': url,
               'com': com}
    return render(request, 'commune.html', context)
