from django.core.cache import cache
from django.http import HttpRequest
from user.models import User
from user.logic import send_message, check_vcode

from lib.http import render_json
from common import err

def get_vertify_code(request:HttpRequest):
    """手机注册"""
    moblie = request.GET.get("mobile")
    send_message(moblie)
    return render_json(data=None,code=0)

def login(request:HttpRequest):
    # 获取手机号
    moblie = request.POST.get("mobile")
    vcode =  request.POST.get("vcode")
    print('from web:', moblie,vcode)
    if check_vcode(moblie,vcode):
        # 获取用户
        user, created = User.objects.get_or_create(phone_number=moblie)
        # 记录登录状态
        request.session['uid'] = user.id
        # 返回用户信息 
        return render_json(data=user.to_dict(),code=0)
    else:
        # 返回出错
        return render_json(data=None,code=err.VCODE_ERROR)
    


def get_profile(request):
    pass


def modified(request):
    pass


def upload_avator(request):
    pass