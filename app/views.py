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

json.dumps(parse.parse_qs("a=1&b=2"))

test_json = {}

def test(request):
    print('test')
    json_response = {
        "messages": [
        ]
    }
    print(request)


    if request.method == 'GET':
        full_path = request.get_full_path().split('?')
        if len(full_path) > 1:
            json_str = json.dumps(parse.parse_qs(full_path[1]))

            json_response['messages'].append({"text": "Getting query:"})
            json_response['messages'].append({"text": json_str }) 
        else:
            json_response['messages'].append({"text": "Getting nothing"})
        
    else:
        try:
            body = json.loads(request.body)
            test_json = body
            print(body)
            json_response['messages'].append({"text": "Echoing:"})
            json_response['messages'].append({"text": str(body) + "body" })
        except:       
            json_response['messages'].append({"text": "Url:" })
            json_response['messages'].append({"text": request.path })

    print(json_response)
    return JsonResponse(json_response)
    

def jsson(request):
    return JsonResponse(test_json)

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Kociaki bot',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )
