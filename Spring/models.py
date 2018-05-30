# coding:utf8
from django.db import models


# 定义数据库表结构
class Test(models.Model):
    username = models.CharField(max_length=50, verbose_name='用户名')

    password = models.CharField(max_length=50, verbose_name='密码')

    nickname = models.CharField(max_length=50, verbose_name='昵称')

    head_pic = models.ImageField(upload_to='head_img/', default='head_img/default.jpg')

    # 重写此方法来制定在admin中的显示的文字
    def __str__(self):
        return self.username