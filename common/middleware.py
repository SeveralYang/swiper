from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from user.models import User
from lib.http import render_json
from common import err

class CorsMiddleware(MiddlewareMixin):
    def process_request(self,request):
        if request.method == 'OPTIONS' and "HTTP_ACCESS_CONTROL_REQUEST_METHOD" in request.META:
            response = HttpResponse()
            response['Content-Length'] = '0'
            response['Access-Control-Allow-Headers'] = request.META['HTTP_ACCESS_CONTROL_REQUEST_METHOD']
            response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8000'
            return response
    
    def process_response(self,request,response):
        response['Access-Control-Allow-Origin'] = 'http://127.0.0.1:8000'
        response['Access-Control-Allow-Credentials'] = 'true'
        return response
    
class AuthMiddleware(MiddlewareMixin):
    """用户登录验证中间件
        功能:如果用户已经登录则通过,否则需要用户登录
    """
    def process_request(self,request):
        uid = request.session.get('uid')
        if uid:
            try:
                request.user = User.objects.get(id=uid)
                return 
            except:
                request.session.flush() 
        return render_json(data=None,code=err.LOGIN_ERR)