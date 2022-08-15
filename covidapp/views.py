from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.http import HttpResponse
from django.urls import reverse

#covid import
from covid import Covid


import os
import json

# home page
def index(request):

    covid = Covid()
    active_total = covid.get_total_active_cases()
    confirmed = covid.get_total_confirmed_cases()
    recovered = covid.get_total_recovered()
    deaths = covid.get_total_deaths()

    cases=covid.get_data()
    cases2= cases[:5]

    country_list =[]
    country_list.append(['Country','Total Cases'])
    for i in cases2:
        get_country = i['country']
        get_cases = i['confirmed']
        country_list.append([get_country, get_cases])


    return render(request, 'index.html', {
        'active_total' : active_total, 'confirmed':confirmed,
        'recovered' : recovered, 'deaths' : deaths,
        'ext_graph':country_list,

    })

# Extract data using COVID package
def extract_covid(request):

    country_input = request.GET.get('username', None)

    covid = Covid()

    if country_input != '':
        country_summary = covid.get_status_by_country_name(country_input)

    else:
        country_summary = {'Error':'Please select a country from dropdown!!'}

    ext = json.dumps(country_summary)

    return HttpResponse(ext, content_type='application/json')
