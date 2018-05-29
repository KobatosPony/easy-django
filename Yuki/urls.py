from django.contrib import admin
from django.urls import path,re_path
from Yuki import views
from django.conf.urls.static import static
from django.conf import settings

# APP的路由分发系统
urlpatterns = [
    path('test/', views.test, name='test'),
    path('test_reg/', views.test_reg, name='test_reg'),
    path('test_login/', views.test_login, name='test_login'),
    re_path('test_pa/(?P<name>(.){1,10})/', views.test_pa)
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 记得加入static和media的url和root目录到path中
