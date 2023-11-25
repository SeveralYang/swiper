from django.core.cache import cache
from django.http import HttpRequest

from common import err
from lib.http import render_json
from social.logic import get_rcmd_users



# Create your views here.

def users(request:HttpRequest):
    # 获取推荐用户
    group_number =int(request.GET.get('group_num',0))
    start_num = group_number * 5
    end_num = start_num + 5
    users = get_rcmd_users(request.user)[start_num:end_num]
    res = [user.to_dict() for user in users]
    return render_json(data=res,code=0)

def crazy(request:HttpRequest):
    pass

def like(request:HttpRequest):
    pass

def dislike(request:HttpRequest):
    pass

def rewind(request:HttpRequest):
    pass

