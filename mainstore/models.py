from django.db import models
from django.urls import reverse


class Catalog(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'catalog'
        verbose_name_plural = 'catalogs'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mainstore:index',
                       args=[self.slug])


class Product(models.Model):
    catalog = models.ForeignKey(Catalog, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='staticfiles/%Y/%m/%d',
                              blank=True, null=True)
    slug = models.SlugField(max_length=200, db_index=True)
    color = models.CharField(max_length=20, blank=True)
    size = models.CharField(max_length=20, blank=True)
    quantity = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    is_new = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mainstore:product_detail',
                       args=[self.id, self.slug])
