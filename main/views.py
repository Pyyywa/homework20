# from django.shortcuts import render
#
# from main.models import Product
#
# def index(request):
#
#     last_products = Product.objects.all().order_by('-дата_добавления')[:5] # Выборка последних 5 товаров
#     for Product in last_products:
#         print(Product.product_name) # Вывод товаров в консоль
#     return render(request, 'main/index.html', {'Последние_товары': last_products})
