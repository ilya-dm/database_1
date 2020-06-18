from django.shortcuts import render

from phones.models import Phone

def show_catalog(request):
    template = 'catalog.html'
    catalog = Phone.objects.all()
    sort = request.GET.get('sort')
    if sort == 'name':
        catalog = catalog.order_by('name')
    elif sort == 'max_price':
        catalog = reversed(catalog.order_by('price'))
    elif sort == 'min_price':
        catalog = catalog.order_by('price')
    context = {'catalog': catalog,
              }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    name= phone.get().name
    price = phone.get().price
    date = phone.get().release_date.__format__('%d.%m.%y')
    lte = phone.get().lte_exists
    image = phone.get().image
    context = {'phone': phone,
               'price': price,
               'model': name,
               'date': date,
               'lte': lte,
               'image': image,}
    return render(request, template, context)
