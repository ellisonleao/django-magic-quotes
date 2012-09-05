# -*- encoding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('caras.citacoes.views',
    url(r'^$', 'index', name='quotes'),
    url(r'^edicoes/(?P<issue_slug>[\w-]+)/(?P<slug>[\w-]+)/$', 'show_quote', name='show_quote'),
    url(r'^edicoes/(?P<issue_slug>[\w-]+)/$', 'issues_quote', name='issues_quote'),
    url(r'^busca/json/', 'ajax_search', name='search_quote_json'),
    url(r'^busca/', 'search', name='search_quote'),
    url(r'^autor/(?P<slug>[\w-]+)/$', 'author', name='author'),
    url(r'^tema/(?P<slug>[\w-]+)/$', 'theme_page', name='theme_page'),
    url(r'^tag/(?P<name>[\w-]+)/$', 'tag_search', name='tag_search'),
)
