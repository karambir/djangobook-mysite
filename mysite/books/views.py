from django.shortcuts import render_to_response
from django.http import HttpResponse
from mysite.books.models import Book


def search_form(request):
    return render_to_response('search_form.html',
            {'page_title': 'Search Form', 'page_heading':'Search for Books'})


def search(request):
   # error = False
    #if 'q' in request.GET:
        #q = request.GET['q']
        #if not q:
            #error = True
        #else:
            #books = Book.objects.filter(title__icontains=q)
            #return render_to_response('search_results.html',
                #{'books': books, 'query': q})
    #return render_to_response('search_form.html',
        #{'error': error})
    errors=[]
    if 'q' in request.GET:
        q=request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q)>20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                    {'books':books, 'query':q, 'page_title': 'Search Results', 'page_heading':'Search Results'})
    return render_to_response('search_form.html',
            {'errors':errors, 'page_title': 'Search Form', 'page_heading':'Search for Books'})
