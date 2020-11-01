from django.shortcuts import render
from .models import Department, Region


# Create your views here.
def country(request):
    """ Metropole page """
    regions = Region.objects.all()
    context = {'regions': regions}
    return render(request, 'country.html', context)


def region(request, region_id):
    """ Regions page """
    depts = Department.objects.filter(region=region_id)
    region = Region.objects.get(id=region_id)
    context = {'depts': depts,
               'region': region}
    return render(request, 'region.html', context)



