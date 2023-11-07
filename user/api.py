from django.core.cache import cache
from user.logic import send_message
from lib.http import render_json

def get_vertify_code(request):
    """手机注册"""
    moblie = request.get("moblie")
    send_message(moblie)
    return render_json(data=None,code=0)

def login(request):
    cache.get('key')
    return 

def get_profile(request):
    pass


def modified(request):
    pass


def upload_avator(request):
    pass