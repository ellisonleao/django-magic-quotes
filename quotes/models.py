# -*- encoding: utf-8 -*-
from django.db import models
from django.conf import settings
from core import Publishable
from taggit.managers import TaggableManager

class Theme(Publishable):
    title = models.CharField(max_length=200,verbose_name=u"Nome do Tema")
    slug = models.SlugField(u"Retranca",max_length=150)
    description = models.TextField(verbose_name=u"Descrição",blank=True,null=True)


    class Meta:
        verbose_name = "Tema"
        verbose_name_plural = "Temas"
        ordering = ['-date_insert']

   
    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('theme_page', () ,{
            'slug': self.slug    
        }) 


    def url(self):
        if self.id:
            return settings.SITE_HOST + self.get_absolute_url()
        else:
            return ''


class Author(Publishable):
    title = models.CharField(max_length=200,verbose_name=u"Nome do Autor")
    slug = models.SlugField(u"Retranca",max_length=255)
    description = models.TextField(verbose_name=u"Descrição",blank=True,null=True)
    image = models.ImageField(verbose_name=u"Imagem",blank=True,null=True)    


    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['-date_insert']

    
    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('author',(), {
            'slug': self.slug
        })


    def url(self):
        if self.id:
            return settings.SITE_HOST + self.get_absolute_url()
        else:
            return ''

    def thumb_admin_list(self):
        if self.photo:
            return """<img src="%s"
                    style="width: 80px;">
                    """ % self.photo.thumb_url()
        else:
            return 'Sem Imagem'
    thumb_admin_list.short_description = 'Foto'
    thumb_admin_list.allow_tags = True


class Quote(Publishable):
    theme = models.ForeignKey(Theme, verbose_name=u"Tema",blank=True,null=True)
    title = models.CharField(u"Título",max_length=255)
    slug = models.SlugField(u"Retranca",max_length=255)
    quote = models.TextField(u"Citação")
    author = models.ForeignKey(Author,verbose_name=u"Autor")
    
    tags = TaggableManager()
 
    class Meta:
        verbose_name = "Citação"
        verbose_name_plural = "Citações"
        ordering = ['-date_insert']

    def __unicode__(self):
        return self.quote

    @models.permalink
    def get_absolute_url(self):
        try:
            issue = self.issue.slug
        except AttributeError:
            issue = 'sem-edicao'

        return ('show_quote', (), {
            'issue_slug': issue,
            'slug': self.slug
        })


    def url(self):
        if self.id:
            return settings.SITE_HOST + self.get_absolute_url()
        else:
            return ''

    def get_tags(self):
        return self.tags.all()


