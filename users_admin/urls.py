"""users_admin URL Configuration

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
from user_profile_api.views import video_feed, video, enviar_solicitud

urlpatterns = [
    path('enviar_solicitud/', enviar_solicitud, name='enviar_solicitud'),
    path('video_feed/', video_feed, name='video_feed'),
    path('video/', video, name='video'),
    path('', admin.site.urls),
]
