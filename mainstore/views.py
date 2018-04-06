from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from cart.form import CartAddProductForm
from mainstore.models import Product, Catalog


def index(request, catalog_slug=None):
    catalog = None
    catalogs = Catalog.objects.all()

    products = Product.objects.all()

    if catalog_slug:
        catalog = get_object_or_404(Catalog, slug=catalog_slug)
        products = products.filter(catalog=catalog)

    # paginator,show 2 products per page
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    pts = paginator.get_page(page)

    cart_product_form = CartAddProductForm()
    context = {
        'catalogs': catalogs,
        'catalog': catalog,
        'products': products,
        'pts': pts,
        'cart_product_form': cart_product_form,

    }

    return render(request, 'mainstore/home1.html', context)


def start_(request, catalog_slug_s=None):
    catalog = None
    catalogs = Catalog.objects.all()

    products = Product.objects.all()
    products = products.filter(is_new='1')

    if catalog_slug_s:
        catalog = get_object_or_404(Catalog, slug=catalog_slug_s)
        products = products.filter(catalog=catalog)

    cart_product_form = CartAddProductForm()

    context = {
        'catalogs': catalogs,
        'catalog': catalog,
        'products': products,
        'cart_product_form': cart_product_form,

    }

    return render(request, 'mainstore/start.html', context)


def product_detail(request, p_id, p_slug):
    product = get_object_or_404(Product, id=p_id, slug=p_slug, available=1)
    catalog = get_object_or_404(Catalog, id=product.catalog_id)

    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
        'catalog': catalog,

    }

    return render(request, 'mainstore/detail.html', context)


def search(request, catalog_slug=None):
    p_name = request.GET.get('mysearch')
    result = None
    catalog = None
    catalogs = Catalog.objects.all()
    products = Product.objects.all()

    if p_name is not None:

        try:
            result = products.filter(name__contains=p_name)
        except result.NoneType:
            print("No search result")
    else:
        result = products
    data = serializers.serialize('json', list(result), fields=('id', 'name', 'image', 'price'))
    request.session['search_result'] = data
    # print("search_result---: ", request.session.get('search_result'))
    # print("data is: ", data)
    # result=request.session.get('search_result')
    page = request.GET.get('page')

    paginator = Paginator(result, 6)

    try:
        pts = paginator.get_page(page)
    except PageNotAnInteger:
        pts = paginator.get_page(1)
    except EmptyPage:
        pts = paginator.get_page(paginator.num_pages)

    cart_product_form = CartAddProductForm()

    context = {
        'catalogs': catalogs,
        'catalog': catalog,
        'products': products,
        'result': result,
        'pts': pts,
        'cart_product_form': cart_product_form,

    }

    return render(request, 'mainstore/search1.html', context)
