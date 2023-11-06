# from django.shortcuts import render 前后端不分离时 返回视图 
# 分离时 返回Json

# Create your views here.
"""
短信验证
获取个人资料
修改个人资料
头像上传
"""


def get_vertify_code(request):
    """手机注册"""
    phone_number = request.get("phone_number")
    
def login(request):
    pass


def get_profile(request):
    pass


def modified(request):
    pass


def upload_avator(request):
    pass
