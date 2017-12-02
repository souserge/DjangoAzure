"""
Definition of views.
"""
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.http import JsonResponse
from django.http import HttpResponse
import json
from urllib import parse
from .models import Pet
import datetime

test_json = {}

def add_pets(request):
    query = get_query(request)
    if request.method == 'GET' and not (query is None):
        return JsonResponse("json_res")

def get_pets(request):
    query = get_query(request)
    if request.method == 'GET' and not (query is None):
        print('Received query: ' + str(query))
        pets = Pet.objects.filter(
            type=query['type'][0].lower(),
            sex=query['sex'][0].lower(),
            location=query['city'][0],
        )
        
        json_res = compose_json(pets)
        print(json.dumps(json_res, indent=4, sort_keys=True))
        return JsonResponse(json_res)


def compose_json(pets):
    DATE = datetime.date.today
    elements = []

    for pet in pets:
        age = DATE - pet.date_of_birth
        elements.append({ 
            "title": pet.name,
            "image_url": "http://561e5a1a.ngrok.io" + pet.photo.url,
            "subtitle": 
                pet.type
                + ", " + ('male' if pet.sex.lower() == 'm' else 'female')
                + ', ' + age + ' y.o.',
        })
    
    return { 
        'messages': [
            {
                'attachment': {
                    "type": "template",
                    "payload": {
                        "template_type":"generic",
                        "image_aspect_ratio": "square",
                        "elements": elements
                    }
                }
            }
        ]
    }
  

def get_query(request):
    full_path = request.get_full_path().split('?')
    if len(full_path) > 1:
        return parse.parse_qs(full_path[1])
    else:
        return None