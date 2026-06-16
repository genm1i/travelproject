from django.contrib.auth.models import User
from .models import Destination, CartItem
from django.shortcuts import render, redirect, get_object_or_404
from .models import Request
from django.contrib.auth import authenticate, login, logout

def index(request):
    query = request.GET.get('q')

    dests = Destination.objects.all()

    if query:
        dests = dests.filter(name__icontains=query)

    total_tours = dests.count()
    hot_tours = dests.filter(offer=True).count()
    hot_offers = dests.filter(offer=True)[:3]

    if total_tours > 0:
        avg_price = sum(d.price for d in dests) // total_tours
    else:
        avg_price = 0

    context = {
        'dests': dests,
        'total_tours': total_tours,
        'hot_tours': hot_tours,
        'avg_price': avg_price,
        'hot_offers': hot_offers,
    }

    return render(request, 'index.html', context)


def tours(request):
    dests = Destination.objects.all()
    return render(request, 'tours.html', {'dests': dests})


def blog(request):
    return render(request, 'blog.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    return render(request, 'contacts.html')


def login_page(request):
    return render(request, 'login.html')


def register_page(request):
    return render(request, 'register.html')

def tour_detail(request, id):
    tour = get_object_or_404(Destination, id=id)
    return render(request, 'tour_detail.html', {'tour': tour})

def send_request(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']

        Request.objects.create(
            name=name,
            phone=phone
        )

    return redirect('/')

def logout_page(request):
    logout(request)
    return redirect('home')

def cart(request):
    if not request.user.is_authenticated:
        return redirect('login')

    items = CartItem.objects.filter(user=request.user)

    return render(request, 'cart.html', {
        'items': items
    })


def add_to_cart(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    tour = get_object_or_404(Destination, id=id)

    CartItem.objects.create(
        user=request.user,
        destination=tour
    )

    return redirect('cart')


def remove_from_cart(request, id):
    item = get_object_or_404(
        CartItem,
        id=id,
        user=request.user
    )

    item.delete()

    return redirect('cart')

def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')

from django.contrib import messages
from django.contrib.auth.models import User


def register_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Проверяем, существует ли пользователь
        if User.objects.filter(username=username).exists():
            messages.error(request, "Такой логин уже существует")
            return render(request, 'register.html')

        # Создаем пользователя
        User.objects.create_user(
            username=username,
            password=password
        )

        messages.success(request, "Аккаунт создан!")
        return redirect('login')

    return render(request, 'register.html')