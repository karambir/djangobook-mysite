from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

def hello(request):
    ua = request.META.get('HTTP_USER_AGENT', 'unknown')
    host = 'http://'+request.get_host()
    values = request.META.items()
    values.sort()
    return render_to_response('home.html', {'page_title' : 'Home', 'page_desc' : 'This is the home page of my django site', 'page_heading' : 'Information Page', 'your_host' : host, 'your_path' : request.path, 'your_agent' :
        ua})
    #return HttpResponse("<html><h1>Hello world</h1><p>My name is nothing. Welcome to the page at %s%s </p><p>Your browser is %s</p></html>"
            #%(request.get_host(), request.path,ua))

def current_datetime(request):
    now = datetime.datetime.now()
    host = 'http://'+request.get_host()
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date': now}))
    # html = "<html><body>It is now %s.</body></html>" %now
    return render_to_response('current_datetime.html', {'page_title' : 'Current Tme', 'page_desc' : 'This page shows the current time and date', 'page_heading' : 'Current Time and Date Page', 'your_host' : host, 'current_date' : now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise HTTP404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('time_ahead.html', {'page_title' : 'Home', 'page_desc' : 'This is the home page of my django site', 'page_heading' : 'Future Time', 'offset' : offset, 'your_path' : request.path, 'dt' :
        dt})

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
    
def set_color(request):
    if "favorite_color" in request.GET:

        # Create an HttpResponse object...
        response = HttpResponse("Your favorite color is now %s" % \
            request.GET["favorite_color"])

        # ... and set a cookie on the response
        response.set_cookie("favorite_color",
                            request.GET["favorite_color"])

        return response
        
    elif "favorite_color" in request.COOKIES:
        return HttpResponse("Your favorite color is %s" % \
            request.COOKIES["favorite_color"])
    else:
        return HttpResponse("You don't have a favorite color.")

