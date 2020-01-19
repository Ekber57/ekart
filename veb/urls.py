"""veb URL Configuration

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
from index import views as index_view
from office import views as office_view
from register import views as register_view
from send_money import views as s_m
from buy_card import views as b_c
from send_card import views as s_c
from change_profile import views as c_p


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view.index),
    path('login', index_view.login),
    path('office', office_view.index),
    path('logout', index_view.logout),
    path('register', register_view.index),
    path('registiration', register_view.registiration),
    path('send_money', s_m.index),
    path('transfer', s_m.transfer),
    path('send_card', s_c.index),
    path('tranzaksiya', s_c.tranzaksiya),
    path('buy_card', b_c.index),
    path('buy_card/transfer', b_c.transfer),
    path('change_profile/', c_p.index),
    path('change_profile/change', c_p.change),
    
    
    
    
    
    
]
