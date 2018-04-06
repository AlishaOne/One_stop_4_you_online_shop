from django.contrib import admin

from mainstore.models import Product, Catalog


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class CatalogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Product,ProductAdmin)
admin.site.register(Catalog,CatalogAdmin)