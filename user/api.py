from django.core.cache import cache
from django.http import HttpRequest
from django.core.cache import cache

from user.models import User
from user.logic import send_message, check_vcode,write_file
from user.form import ProfileForm
from lib.http import render_json
from common import err

def get_vertify_code(request:HttpRequest):
    """手机注册"""
    moblie = request.GET.get("mobile")
    send_message(moblie)
    return render_json(data=None,code=0)

def login(request:HttpRequest):
    moblie = request.POST.get("mobile")
    vcode =  request.POST.get("vcode")
    print('from web:', moblie,vcode)
    if check_vcode(moblie,vcode):
        # 获取用户 or 创建新用户
        user, created = User.objects.get_or_create(phone_number=moblie)
        
        if created:
            pass

        # 记录登录状态, 登录成功则为request.session添加uid
        request.session['uid'] = user.id
        # 返回用户信息 
        return render_json(data=user.to_dict(),code=0)
    else:
        # 返回出错
        return render_json(data=None,code=err.VCODE_ERROR)
    
def get_profile(request:HttpRequest):
    """
    为了记录会话状态
    session 即会话 保存在服务器端 
    cookie 以文件的形式保存在浏览器端_本地, 用户可以读写所以不安全
    """
    user = request.user
    key_profile = f"{user.id}_profile"
    user_profile  = cache.get(key_profile)
    # print('load from cache',user_profile)
    if not user_profile:
        user_profile = user.profile.to_dict()
        # print('load from User.model',user_profile)
        cache.set(key=key_profile,value=user_profile) 
      
    return render_json(data=user.profile.to_dict(),code=0)

def modified(request:HttpRequest):
    """
    修改user所拥有的profile
    django.forms 用于验证提交数据是否符合格式要求
    """
    #  form= ProfileForm(request.POST) 不能直接使用  form= ProfileForm(request.POST)
    form = ProfileForm(instance=request.user.profile, data=request.POST)
    if form.is_valid(): # django封装 用于验证提交数据是否符合格式要求
        form.save()  # django封装 用于提交符合格式要求的数据
        """
        等价于
        request.user.profile.__dict__.update(form.cleaned_data)
        request.user.profile.save()
        """
        # 更新缓存
        key_profile = f"{request.user.id}_profile"
        cache.set(key=key_profile,value=request.user.profile) 
        return render_json(data=None,code=0)
    else:
        return render_json(data=form.errors,code = err.PROFILE_DATA_ERROR)

def upload_avator(request:HttpRequest):
   
    uid = request.user
    # 获取上传图片
    file =  request.FILES.get('avatar')
    if file : # and  check_image()
        # 保存图片到本地; 上传图片到七牛服务器; 并返回url地址
        url = write_file(file,uid)
        return render_json(data={"msg":f"{url}"},code=0)
    else:
        return render_json(data=None,code=err.AVATAR_UPLOAD_ERROR)