# -*- encoding: utf-8 -*-

from django.contrib import admin
from caras.citacoes.models import Quote,Author,Theme


def action_publish(modeladmin, request, queryset):
    queryset.update(published=True)
action_publish.short_description = u"Marcar selecionados como Publicados"


def action_unpublish(modeladmin, request, queryset):
    queryset.update(published=False)
action_unpublish.short_description = u"Marcar selecionados como Não-Publicados"


class QuoteAdmin(admin.ModelAdmin):
    model = Quote
    actions = [action_publish, action_unpublish]
    list_display = ['issue','author','quote', 'date_available', 'published']
    list_display_links = ['issue']
    list_filter = ['issue', 'published', 'date_available']
    raw_id_fields = ['issue','author','theme']
    prepopulated_fields = {"slug": ("title",)}

    fieldsets = (
        (u'Informações', {
            'fields': ('issue','author','theme','title','slug','quote','tags')}),
        (u'Publicação', {
            'classes': ('extrapretty'),
            'fields': ('published', 'date_available')}),
    )

admin.site.register(Quote, QuoteAdmin)



class AuthorAdmin(admin.ModelAdmin):
    model = Author
    actions = [action_publish, action_unpublish]
    list_display = ['thumb_admin_list','title', 'date_available', 'published']
    prepopulated_fields = {"slug": ("title",)}
    search_fields =['title',]
    raw_id_fields = ['photo',]
    fieldsets = (
        (u'Informações', {
            'fields': ('title','slug','description','photo')}),
        (u'Publicação', {
            'classes': ('extrapretty'),
            'fields': ('published', 'date_available')}),
    )

admin.site.register(Author,AuthorAdmin)


class ThemeAdmin(admin.ModelAdmin):
    model = Theme
    actions = [action_publish, action_unpublish]
    list_display = ['title', 'date_available', 'published']
    search_fields =['title',]
    prepopulated_fields = {"slug": ("title",)}
    
    fieldsets = (
        (u'Informações', {
            'fields': ('title','slug','description')}),
        (u'Publicação', {
            'classes': ('extrapretty'),
            'fields': ('published', 'date_available')}),
    )


admin.site.register(Theme,ThemeAdmin)



