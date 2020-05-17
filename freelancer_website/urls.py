"""freelancer_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from user_accounts.views import user_login, logout, user_account, signup
from freelancer_website.views import index
from quote.views import quote, quote_logged
from basket.views import basket, add_to_basket, remove_from_basket
from checkout.views import checkout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name="login"),
    path('logout/', logout, name="logout"),
    path('user_account/', user_account, name="user_account"),
    path('', index, name="index"),
    path('registration/', signup, name="signup"),
    path('quote/', quote, name="quote" ),
    path('quote_logged/', quote_logged, name="quote_logged"),
    path('basket/', basket, name="basket"),
    path('add_to_basket/', add_to_basket, name="add_to_basket"),
    path('remove_from_basket/', remove_from_basket, name="remove_from_basket" ),
    path('checkout/', checkout, name="checkout")
]
