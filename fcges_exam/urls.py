"""
URL configuration for fcges_exam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from test_a.views import Exam1View, Exam2View, Exam3View

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('find_missing_int/', Exam1View.as_view(), name='find_missing_int'),
    path('find_divisible/', Exam2View.as_view(), name='find_divisible'),
    path('rotate/', Exam3View.as_view(), name='rotate'),
    path('trading_system/', include('trading_system.urls')),
]
