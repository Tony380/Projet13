from django.shortcuts import render
from .models import Department, Region
import wikipedia

wikipedia.set_lang("fr")


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
        wiki_page = wikipedia.summary(region.name, 4)
        wiki = wikipedia.page(region.name).url
    except wikipedia.DisambiguationError:
        wiki_page = wikipedia.page(region.name + '(région administrative)').summary
        wiki = wiki_page.url
    context = {'depts': depts,
               'region': region,
               'wiki': wiki_page,
               'wi': wiki}
    return render(request, 'region.html', context)
