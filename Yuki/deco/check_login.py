# coding=utf8
from django.shortcuts import render_to_response, redirect


# 定义总装饰器（拥有前后各一个装饰函数）
def deco_double(before_func, after_func):
    def outer(main_fun):
        def wrapper(request, *args, **kwargs):
            before_result = before_func(request, *args, **kwargs)
            if before_result is not None:
                return before_result

            main_result = main_fun(request, *args, **kwargs)
            if main_result is not None:
                return main_result

            after_result = after_func(request, *args, **kwargs)
            if after_result is not None:
                return after_result
        return wrapper
    return outer


# 装饰函数在前执行
def deco_before(before_func):
    def outer(main_fun):
        def wrapper(request, *args, **kwargs):
            before_result = before_func(request, *args, **kwargs)
            if before_result is not None:
                return before_result

            main_result = main_fun(request, *args, **kwargs)
            if main_result is not None:
                return main_result
        return wrapper
    return outer


# 装饰函数在之后执行
def deco_after(after_func):
    def outer(main_fun):
        def wrapper(request, *args, **kwargs):
            main_result = main_fun(request, *args, **kwargs)
            if main_result is not None:
                return main_result

            after_result = after_func(request, *args, **kwargs)
            if after_result is not None:
                return after_result
        return wrapper
    return outer


# 检测登录状态装饰器函数
def check_login(request):
    try:
        se_user = request.session['login']['user']
    except Exception as e:
        se_user = None
    co_user = request.COOKIES.get('username',None)
    is_login = request.COOKIES.get('is_login',0)
    if se_user != co_user:
        ret = {'msg':"请先登录！"}
        return render_to_response('signup_login.html',{"ret_data":ret})

    elif not is_login:
        ret = {'msg':"请先登录！"}
        return render_to_response('signup_login.html',{"ret_data":ret})

    else:
        return None