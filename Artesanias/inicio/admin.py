from django.contrib import admin
from .models import Artesanias
from .models import OpinionArtesania

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('nombre', 'municipio','costo', 'created')
    search_fields= ('nombre', 'municipio')
    date_hierarchy = 'created'
    list_filter = ('nombre','costo')

    list_per_page=2
    list_display_links=( 'nombre',)
    list_editable= ('costo',)
admin.site.register(Artesanias, AdministrarModelo)

class AdministrarOpiniones(admin.ModelAdmin):
    list_display = ('id', 'artesania')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
admin.site.register(OpinionArtesania, AdministrarOpiniones)
