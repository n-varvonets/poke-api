"""poke_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

# from core.views import index_page # first not actual version hardcore import view from an app
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index_page),  # ПРРОБЛЕМА:если сотни вьюх из разньіх 'app', то здесь будет бардак,
    # РЕШЕНИЕ: проще обращаться к конкретному 'арр' внутри файла urls - разделение логики: include
    path('', include('core.urls'))
]
