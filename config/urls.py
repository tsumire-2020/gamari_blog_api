
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
  #本番で使用したくない場合はここを削除
    path('admin/', admin.site.urls),

    path("auth/", include("djoser.urls.jwt")),
]


