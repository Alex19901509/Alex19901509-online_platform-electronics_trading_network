from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .models import Supplier, Product, NetworkNode
from .serializers import SupplierSerializer, ProductSerializer, NetworkNodeSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    filter_backends = (DjangoFilterBackend,)  # Добавляем поддержку фильтров
    filterset_fields = ['country']  # Указываем, что можно фильтровать по стране


def add_supplier(request):
    if request.method == 'POST':
        new_supplier = Supplier(
            name=request.POST['name'],
            email=request.POST['email'],
            country=request.POST['country'],
            city=request.POST['city'],
            street=request.POST['street'],
            house_number=request.POST['house_number'],
        )
        new_supplier.save()
        return redirect('add_supplier')
    return render(request, 'network/supplier_form.html')


def add_product(request):
    if request.method == 'POST':
        new_product = Product(
            name=request.POST['name'],
            model=request.POST['model'],
            release_date=request.POST['release_date'],
        )
        new_product.save()
        return redirect('add_product')
    return render(request, 'network/product_form.html')


def add_network_node(request):
    suppliers = Supplier.objects.all()
    products = Product.objects.all()
    if request.method == 'POST':
        new_node = NetworkNode(
            name=request.POST['name'],
            email=request.POST['email'],
            country=request.POST['country'],
            city=request.POST['city'],
            street=request.POST['street'],
            house_number=request.POST['house_number'],
            product_id=request.POST['product'],
            supplier_id=request.POST.get('supplier', None),
            debt=request.POST['debt'],
            level=request.POST['level'],
        )
        new_node.save()
        return redirect('add_network_node')
    return render(request, 'network/network_node_form.html', {'suppliers': suppliers, 'products': products})


def home(request):
    return render(request, 'network/home.html')


@login_required
def home(request):
    return render(request, 'home.html')


def landing_page(request):
    if request.user.is_authenticated:
        return redirect('home')  # Перенаправление на главную страницу для авторизованных пользователей
    else:
        return redirect('login')  # Перенаправление на страницу входа для неавторизованных пользователей


@login_required
def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу входа после успешной регистрации
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})