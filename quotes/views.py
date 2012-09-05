# -*- encoding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.exceptions import MultipleObjectsReturned

from tagging.fields import TagField
from tagging.models import Tag,TaggedItem

from caras.citacoes.models import Quote,Author,Theme
from caras.website.models import Issue

import simplejson


def index(request):
    """
    Página das citacoes
    """
    quotes = Quote.objects.filter(
        published=True,
    )[:6]
    #most_commented = Quote.get_most_commented()
   
    return render(request,'citacoes/index.html',{
            'quotes':quotes,
            #'most_commented':most_commented
        })


def author(request,slug):
    """
    Página de autor
    """
    try:
        author = get_object_or_404(Author,slug=slug)
    except MultipleObjectsReturned:
        author = Author.objects.filter(slug=slug)[0]
    
    author_quotes = Quote.objects.filter(published=True,author=author)
    #most_commented = Quote.get_most_commented()
    return render(request,'citacoes/author.html',{
            'author': author,
            'author_quotes':author_quotes,
            #'most_commented':most_commented,
        })


def ajax_search(request):
    """
    Retorna resultado de busca por autor, nome da citacao e 
    conteudo da citacao
    """
    result = {}
    result['status'] = False
    q = request.GET.get('term',None)
    if q:
        authors = Author.objects.filter(published=True,title__icontains = q)[:3]
        quotes = Quote.objects.filter(Q(published=True) & Q(title__icontains = q) | \
            Q(quote__icontains = q) | Q(author__title__icontains=q))[:3]
        themes = Theme.objects.filter(published=True,title__icontains=q)[:3]

        l_author = []
        for a in authors:
            l_author.append({'title': a.title, 'slug': a.get_absolute_url()})

        l_quote = []
        for q in quotes:
            l_quote.append({'quote': q.quote, 'slug': q.get_absolute_url()})

        l_theme = []
        for t in themes:
            l_theme.append({'title': t.title, 'slug': t.get_absolute_url()})

        result['authors'] = l_author
        result['quotes'] = l_quote
        result['themes'] = l_theme
        result['status'] = True
    
    return HttpResponse(simplejson.dumps(result), mimetype="application/json")
        


def search(request):
    """
    Página de resultado da busca
    """
    q = request.GET.get('term',None)
    result = {}
    if q:
        authors = Author.objects.filter(published=True,title__icontains = q)
        quotes = Quote.objects.filter(Q(published=True) & Q(title__icontains = q) | \
            Q(quote__icontains = q) | Q(author__title__icontains=q))

        themes = Theme.objects.filter(published=True,title__icontains=q)
        
        result['authors'] = authors
        result['quotes'] = quotes
        result['themes'] = themes

        nresult = result['quotes']
    return render(request,'citacoes/search.html',{
            'result':nresult
        })



def tag_search(request,name=False):
    """
    Página de busca de tag
    """
    tag_name = name
    #most_commented = Quote.get_most_commented()
    quotes = []
    if tag_name:
        try:
            tag = Tag.objects.get(name=tag_name)
            quotes = TaggedItem.objects.get_union_by_model(Quote,tag)
        except Tag.ObjectDoesNotExist:
            pass

    return render(request,'citacoes/tag_search.html',{
            'quotes':quotes,
            'tag_name':tag_name,
            #'most_commented':most_commented,
        })


def theme_page(request,slug):
    """
    Página de citacoes de um determinado tema
    """
    theme = get_object_or_404(Theme,slug=slug)
    quotes = Quote.objects.select_related().filter(published=True,theme__slug = slug)
    #most_commented = Quote.get_most_commented()
    return render(request,'citacoes/theme_page.html',{
            'theme':theme,
            'quotes':quotes,
            #'most_commented':most_commented,
        })


def issues_quote(request,issue_slug):
    """
    Página de citacoes de uma revista
    """
    issue = get_object_or_404(Issue,slug=issue_slug)
    quotes = Quote.objects.filter(published=True,issue__slug = issue_slug)
    #most_commented = Quote.get_most_commented()
    return render(request,'citacoes/issues_quote.html',{
            'quotes':quotes,
            'issue':issue,
            #'most_commented':most_commented,
        })


def show_quote(request,issue_slug,slug):
    """
    Página de uma citacao
    """

    issue = get_object_or_404(Issue,slug=issue_slug)

    if issue_slug != 'sem-edicao':
        quote = get_object_or_404(Quote,slug=slug,issue__slug=issue_slug)
    else:
        quote = get_object_or_404(Quote,slug=slug)
    
    #most_commented = Quote.get_most_commented()
    return render(request,'citacoes/show_quote.html',{
        'quote':quote,
        'issue':issue
        #'most_commented':most_commented,
    })
