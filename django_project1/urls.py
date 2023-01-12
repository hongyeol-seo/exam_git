"""django_project1 URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('blog/', include('blog.urls'))
    # include는 찾은 url 패턴에 대해 다른 urls 파일로 넘겨주는 역할을 합니다.
    # 제가 만든 Django 프로젝트의 프로젝트 디렉토리에 있는 urls.py는 다음과 같습니다.
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
