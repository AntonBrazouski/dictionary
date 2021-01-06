from django.shortcuts import render, HttpResponse
from django.views import generic

from .models import Meaning, Token




class IndexView(generic.ListView):
    template_name = 'words/index.html'
    context_object_name = 'query'

    def get_queryset(self):
        return Token.objects.all()[:2]


class DetailView(generic.DeleteView):
    model = Token
    context_object_name = 'query'
    template_name= 'words/detail.html'



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
