from datetime import datetime
from user.models import User
from social.models import Swiped,Friend

def get_rcmd_users(user:User):
    sex = user.profile.date_sex
    location = user.profile.location
    now_year = datetime.today().year
    min_year = now_year - user.profile.max_data_age 
    max_year = now_year- user.profile.min_data_age 
    users = User.objects.filter(
        location=location,
        sex=sex,
        birth_year__gte=min_year,
        birth_year__lte=max_year
    )
    return users

def like_operate(uid,sid):
    """喜欢一个用户的操作"""
    # 添加滑动喜欢状态
    Swiped.mark(uid,sid,'like')
    # 查看对方是否喜欢自己
    if Swiped.is_liked(sid,uid):
        Friend.be_friend(uid,sid)
        return True
    else:
        return False


def crazy_operate(uid,sid):
    """超级喜欢一个用户的操作"""
    Swiped.mark(uid,sid,'crazy')
    # 查看对方是否喜欢自己
    if Swiped.is_liked(sid,uid):
        Friend.be_friend(uid,sid)
        return True
    else:
        return False

def dislike_operate(uid,sid):
    Swiped.mark(uid,sid,'dislike')
    Friend.remove_friend(uid, sid)


def rewind_operate(uid,sid):
    # 取消滑动记录
    try:
        Swiped.objects.get(uid =uid, sid = sid).delete()
    except Swiped.DoesNotExist:
        pass
    # 删除好友关系 如果不是好友则会pass
    Friend.remove_friend(uid, sid)
