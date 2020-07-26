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
from contact.views import contact
from quote.views import quote, quote_logged, reupload, accept, accept_quote
from basket.views import basket, add_to_basket, remove_from_basket
from checkout.views import checkout, payment
from chat.views import chat, chat_send
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include


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
    path('checkout/', checkout, name="checkout"),
    path('payment/', payment, name="payment"),
    path('reupload/<int:quote_ref>/<str:file_name>/', reupload, name="reupload"),
    path('chat_send/', chat_send, name="chat_end"),
    path('chat/<int:quote_ref>/<str:file_name>/', chat, name="chat"),
    path('accept/<int:quote_ref>/<str:file_name>', accept, name="accept"),
    path('accept_quote/<int:quote_ref>', accept_quote, name="accept_quote"),
    path('contact/', contact, name="contact"),

    #################################################################################################################
    #thatks to https://stackoverflow.com/questions/11501837/resetting-password-in-django solution 0 
    #just suitted me better......:)
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
           auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),
    ##################################################################################################################
    
]
