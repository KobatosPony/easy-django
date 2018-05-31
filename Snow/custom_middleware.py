# 自定义中间件
import time
from django.utils.deprecation import MiddlewareMixin

class custom_middleware(MiddlewareMixin):
    def process_request(self,request):
        print(time.time())