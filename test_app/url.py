from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('test', views.test,name="test"),
    path('result', views.result,name="result"),
    ]