from django.http import HttpRequest

from lib.http import render_json
from social.logic import get_rcmd_users, like_operate, crazy_operate, dislike_operate, rewind_operate
from social.models import Friend
from vip.logic import permission_required


# Create your views here.

def users(request:HttpRequest):
    # 获取推荐用户
    group_number =int(request.GET.get('group_num',0))
    start_num = group_number * 5
    end_num = start_num + 5
    users = get_rcmd_users(request.user)[start_num:end_num]
    res = [user.to_dict() for user in users]
    return render_json(data=res,code=0)


def like(request:HttpRequest):
    """喜欢"""
    # 更新数据集 记录
    sid = int(request.POST.get('sid'))
    is_match= like_operate(request.user.id,sid)
    return render_json(data={"is_match":is_match},code=0)

@permission_required("crazy_permission")
def crazy(request:HttpRequest):
    """超级喜欢"""
    sid = int(request.POST.get('sid'))
    is_match= crazy_operate(request.user.id,sid)
    return render_json(data={"is_match":is_match},code=0)

def dislike(request:HttpRequest):
    """不喜欢"""
    sid = int(request.POST.get('sid'))
    dislike_operate(request.user.id,sid)
    return render_json(None,0)

@permission_required("rewind_permission")
def rewind(request:HttpRequest):
    """反悔 = 删除所有关系 包括好友关系"""
    sid = int(request.POST.get('sid'))
    rewind_operate(request.user.id,sid)
    return render_json(None, 0)

def list_friends(request:HttpRequest):
    """反悔 = 删除所有关系 包括好友关系"""
    friends = Friend.list_friends(request.user.id)
    friends_info = [frd.to_dict() for frd in friends]
    return render_json(friends_info, 0)

