from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import views as auth_views
from .views import SupplierViewSet, ProductViewSet, NetworkNodeViewSet, home, landing_page, login_view
from .views import add_supplier, add_product, add_network_node
from .views import register

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)
router.register(r'network-nodes', NetworkNodeViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('add-supplier/', add_supplier, name='add_supplier'),
    path('add-product/', add_product, name='add_product'),
    path('add-network-node/', add_network_node, name='add_network_node'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', landing_page, name='landing_page'),  # Переход на главную страницу
    path('login/', login_view, name='login'),  # URL для входа
    path('home/', home, name='home'),  # Главная страница для авторизованных пользователей
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]
