from django.shortcuts import render, render_to_response, redirect
from Yuki import models
from django.db import transaction
from django.http import FileResponse
from django.conf import settings
from django.core.cache import caches,cache

def test(request):
    ret = {}
    username = request.COOKIES.get('user')
    if request.COOKIES.get('user'):
        user = models.Test.objects.all().get(username=username)
        ret['user'] = user
        return render_to_response('test.html', ret)

    else:
        return render_to_response('test.html')


def test_reg(request):
    if request.method == 'GET':
        return render_to_response('test_register.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        nickname = request.POST.get('nickname')
        head_img = request.FILES.get('upload_file')

        # 数据库操作
        # transaction.atomic封装原子操作
        with transaction.atomic():
            models.Test.objects.all().create(username=username, password=password, nickname=nickname, head_pic=head_img)

        return render_to_response('test.html')


def test_login(request):
    if request.method == 'GET':
        return render_to_response('test_login.html')

    if request.method == 'POST':
        ret = {}
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 判断用户是否存在
        user = models.Test.objects.all().filter(username=username, password=password)
        if user.exists():
            request.session['login'] = {'username':username}

            ret['user'] = user
            response = redirect('/yuki/test', ret)
            response.set_cookie('user', username)
            return response


# 下载文件的测试
def test_down_file(request):
    file = open(settings.UR, 'rb')
    return render_to_response('test.html')
    # response = FileResponse(file)
    # response['Content-Type'] = 'application/octet-stream'
    # response['Content-Disposition'] = 'attachment;filename="example.tar.gz"'
    # return response


def test_pa(request,*args,**kwargs):
    print(kwargs['name'])
    return render_to_response('test.html')
