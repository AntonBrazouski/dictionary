from django.shortcuts import render, HttpResponse

from .models import Meaning, Token




def index(request):
    query = Token.objects.all()[:2]
    context = {'query': query }

    return render(request, 'words/index.html', context)


def detail(request, pk):
    query = ""
    error = None
    try:
        query = Token.objects.get(pk=pk)
    except:
        error = "Does not exist"
    context = {'query': query, 'error': error}

    return render(request, 'words/detail.html', context)


def search(request):
    context = {}
    query, error, query_set = ('','','')
    try:
        query = Token.objects.filter(word=request.GET['search'])
        if len(query) == 1:
            query = query[0]
        else:
            query_set = Token.objects.filter(word__contains=request.GET['search'])
            if len(query_set) == 0:
                error = 'Nothing found'
    except:
        error = 'Nothing found..'
    context = {'query': query, 'query_set': query_set, 'error': error}

    return render(request, 'words/search.html', context)
