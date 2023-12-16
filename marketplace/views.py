from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from django.core.paginator import Paginator
from .forms import UserRegistrationForm, MyLoginForm, NameForm, GoodForm, StorageForm
from .models import Client, Order1, OrderStruct, Goods, Delivery, Storage, HasOrderStruct
from .serializers import ClientSerializer, OrderSerializer, OrderStructSerializer, StorageSerializer, GoodsSerializer, \
    DeliverySerializer

menu = [{'title': "Личный кабинет", 'url_name': 'clients'},
        {'title': "Заказы", 'url_name': 'orders'},
        {'title': "Товары", 'url_name': 'goods'},
        {'title': "Склады", 'url_name': 'storages'},
        {'title': "Доставки", 'url_name': 'deliveries'},
]



class ClientList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class OrderList(generics.ListAPIView):
    queryset = Order1.objects.all()
    serializer_class = OrderSerializer


class OrderStructList(generics.ListAPIView):
    queryset = OrderStruct.objects.all()
    serializer_class = OrderStructSerializer


class StorageList(generics.ListAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class DeliveryList(generics.ListAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class GoodsList(generics.ListAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer


@login_required
def clients(request):
    idc = request.user.id_client.id_client
    posts = Client.objects.filter(id_client=idc).all()
    return render(request, 'marketplace/temp/clients.html', {'posts': posts, 'menu': menu, 'title': 'Клиенты'})


def goods(request):
    posts = Goods.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        form = GoodForm(request.POST)
        if form.is_valid():
            # Создаем экземпляр модели и сохраняем его в базе данных
            good_instance = Goods(
                good_name=form.cleaned_data['good_name'],
                short_info=form.cleaned_data['short_info'],
                good_price=form.cleaned_data['good_price']
            )
            good_instance.save()
            return redirect('goods')  # Перенаправляем, например, на страницу успеха
    else:
        form = GoodForm()
    return render(request, 'marketplace/temp/goods.html', {'page_obj': page_obj,'form':form,'posts': posts, 'menu': menu, 'title': 'Товары'})


@login_required
def orders(request):
    idc = request.user.id_client.id_client
    posts = Order1.objects.select_related('id_client').filter(id_client=idc).all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'marketplace/temp/orders.html', {'page_obj': page_obj,'posts': posts, 'menu': menu, 'title': 'Заказы'})


def storages(request):
    posts = Storage.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == 'POST':
        form = StorageForm(request.POST)
        if form.is_valid():
            storage_instance = Storage(
                locate=form.cleaned_data['locate'],
                worktime=form.cleaned_data['worktime']
            )
            storage_instance.save()
            return redirect('storages')  # Перенаправляем, например, на страницу успеха
    else:
        form = StorageForm()
    return render(request, 'marketplace/temp/storages.html', {'page_obj': page_obj,'form':form,'posts': posts, 'menu': menu, 'title': 'Склады'})


@login_required
def deliveries(request):
    idc = request.user.id_client.id_client
    posts = Delivery.objects.filter(id_order__id_client=idc).all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'marketplace/temp/deliveries.html', {'page_obj': page_obj,'posts': posts, 'menu': menu, 'title': 'Доставки'})


@login_required
def order_detail(request, order_id):
    posts = HasOrderStruct.objects.all()
    goods = Goods.objects.all()
    print(posts)
    # if not request.user:
    #     return render(request, 'marketplace/temp/access_denied.html')
    # if request.method == 'POST':
    #     form = NameForm(request.POST)
    #     if form.is_valid():
    #         # Обработка валидной формы
    #         # Сохранение данных в базу данных, выполнение дополнительных действий и т.д.
    #         print(form['prod_cnt'].value())
    #         print(form['good_id'].value())
    #         if Goods.objects.filter(id_good=form['good_id'].value()):
    #             goods_instance = get_object_or_404(Goods, id_good=form.cleaned_data['good_id'])
    #             print("succes")
    #             a = OrderStruct(count_of_prod=form.cleaned_data['prod_cnt'], id_good=goods_instance)
    #             a.save()
    #             print(a)
    #             b = HasOrderStruct(order_id=order_id, order_struct=a)
    #             b.save()
    #             print(b)
    #         else:
    #             print("error")
    #             form.add_error('good_id','Товар с указанным id не найден.')
    #             return render(request, 'marketplace/temp/ord_struct.html',
    #                           {'posts': posts, 'goods': goods, 'menu': menu, 'order_id': order_id, 'form': form})
    #         return redirect('orders')
    # else:
    #     form = NameForm()



    return render(request, 'marketplace/temp/ord_struct.html', {'posts': posts,'goods':goods, 'menu': menu, 'order_id': order_id} )

def index(request):
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }

    return render(request, 'marketplace/temp/index.html', context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Создаем пользователя
            user = form.save()

            # Создаем клиента
            client = Client.objects.create(
                first_name=form.cleaned_data['first_name'],
                second_name=form.cleaned_data['second_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                locate=form.cleaned_data['locate'],
                birthday=form.cleaned_data['birthday'],
            )

            # Связываем пользователя и клиента
            user.id_client = client
            user.save()

            # Логиним пользователя
            login(request, user)

            return redirect('index')
    else:
        form = UserRegistrationForm()

    return render(request, 'marketplace/temp/reg.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = MyLoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Перенаправление после успешного входа
            else:
                messages.error(request, "Invalid username or password. Please try again.")
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = MyLoginForm()

    return render(request, 'marketplace/temp/login.html', {'form': form})

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")

    else:
        form = NameForm()
    return render(request, "marketplace/temp/access_denied.html", {"form": form})

def search(request):
    query = request.GET.get('search', '')  # Получаем значение запроса из параметра 'search' в URL
    # Замените YourProductModel на вашу модель товаров

    if query:
        posts = Goods.objects.filter(good_name=query).all()  # Фильтруем товары по имени

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'marketplace/temp/goods.html',
                  {'page_obj': page_obj, 'posts': posts, 'menu': menu, 'title': 'Товары'})



def storage_search(request):
    query = request.GET.get('search', '')  # Получаем значение запроса из параметра 'search' в URL
    # Замените YourProductModel на вашу модель товаров

    if query:
        posts = Storage.objects.filter(locate=query).all()  # Фильтруем товары по имени

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'marketplace/temp/storages.html',
                  {'page_obj': page_obj, 'posts': posts, 'menu': menu, 'title': 'Склады'})
