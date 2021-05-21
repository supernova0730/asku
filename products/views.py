from django.shortcuts import render
from pprint import pprint
from . import rs24_api as api


def product_list(request):
    page = int(request.GET.get('page', 1))

    storages = api.get_storages()['Stocks']
    samara_id = api.get_storage_by_city('Самара')['ORGANIZATION_ID']

    resp = api.get_positions_in_stock(samara_id, page)
    _items = resp['items'][0][:9]
    last_page = resp['meta']['last_page']

    items = list()

    for item in _items:
        item_code = int(item['CODE'])

        item_price = api.get_prices(item_code)['Price']['Retail']
        item['PRICE'] = '{:.2f}'.format(item_price)

        images = api.get_specs(item_code)['img']
        item['IMAGE_URL'] = images[0]['URL']

        items.append(item)

    context = {
        'items': items,
        'page': page,
        'last_page': last_page
    }

    return render(request, 'products/list.html', context)


def product_detail(request, position_code):
    return render(request, 'products/detail.html')


def basket(request):
    return render(request, 'basket/basket.html')


def basket_form(request):
    return render(request, 'basket/basket-form.html')


def index(request):
    return render(request, 'other/index.html')


def reviews(request):
    return render(request, 'other/reviews.html')


def about(request):
    return render(request, 'other/about.html')


def contacts(request):
    return render(request, 'other/contacts.html')
