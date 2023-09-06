from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Content, Taxonomy, TaxonomyTerroristGroup


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    pass

@admin.register(Taxonomy)
class TaxonomyAdmin(admin.ModelAdmin):
    pass

class MyAdmin(TreeAdmin):
    form = movenodeform_factory(TaxonomyTerroristGroup)

admin.site.register(TaxonomyTerroristGroup, MyAdmin)