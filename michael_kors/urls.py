"""michael_kors URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from michael_kors import settings
from product import views
from product.views import ProductViewSet

schema_view = get_schema_view(
    openapi.Info(
        title='python18 Shop project',
        description='Интернет магазин',
        default_version='v1',
    ),
    public=True
)


api_urlpatterns = [
    path('/account/', include('account.urls')),
    path('/product/', include('product.urls')),
    path('/order/', include('order.urls')),
    # path('single/<int:pk>/', views.new_single, name="new_single"),
]

main_patterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger')),
    path("api/v1", include(api_urlpatterns))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = main_patterns + api_urlpatterns

