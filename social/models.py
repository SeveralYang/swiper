from django.db import models
from user.models import User

# Create your models here.
class Swiped(models.Model):
    STATUS = (
        ("crazy",'超级喜欢'),
        ("like",'喜欢'),
        ("dislike",'不喜欢')
    )
    uid = models.IntegerField(verbose_name='滑动者uid')
    sid = models.IntegerField(verbose_name='被滑动者uid')
    status = models.CharField(max_length=8,choices=STATUS)
    time = models.DateTimeField(auto_now_add=True)

    @classmethod # 类方法 
    def mark(cls,uid,sid,status):
        """添加一条数据"""
        if status in ("crazy","like","dislike"):
            # 如果有则更新status 如果没有则创建
            cls.objects.update_or_create(uid = uid,sid = sid,defaults={"status":status})
        else:
            pass
    
    @classmethod
    def is_liked(cls,uid,sid):
       """
       uid 是否喜欢 sid
       """
       return cls.objects.filter(uid=uid, sid=sid, status__in=('like','crazy')).exists()


class Friend(models.Model):
    """
    uid1 和 uid2 相互喜欢 则成为好友
    uid1 < uid2
    """
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()

    @classmethod
    def be_friend(cls,uid1,uid2):
        # 排序
        uid1,uid2 = (uid1,uid2) if uid1 < uid2 else (uid2,uid1)
        # 新建
        cls.objects.get_or_create(uid1=uid1,uid2=uid2)
    
    @classmethod
    def remove_friend(cls,uid1,uid2):
        uid1,uid2 = (uid1,uid2) if uid1 < uid2 else (uid2,uid1)
        try:
            cls.objects.get(uid1=uid1,uid2=uid2).delete()
        except cls.DoesNotExist:
            pass

    @classmethod
    def is_friend(cls,uid1,uid2):
        condition  = models.Q(uid1=uid1, uid2=uid2)| models.Q(uid1=uid2, uid2=uid1)
        return cls.objects.filter(condition).exists()

    @classmethod
    def list_friends(cls,uid):
        """返回uid用户所有的好友"""
        condition  = models.Q(uid1=uid)| models.Q(uid2=uid)
        relations =  cls.objects.filter(condition)
        friends_id_list = []
        for r in relations:
            friends_id_list.append(r.uid1 if r.uid1 != uid else r.uid2)
        
        return User.objects.filter(id__in = friends_id_list)

