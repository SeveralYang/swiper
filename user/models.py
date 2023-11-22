import datetime
from django.db import models
from django.utils.functional import cached_property
from lib.orm import ModelMixin # Minin 用于实现将数据库信息转化为json功能

class User(models.Model, ModelMixin):
    """
    用户数据模型
    """
    SEX = (
        ('M', '男'),
        ('F', '女')
        # 第一项为记录到数据库中的值，第二项为提升选择的值
    )
    nick_name = models.CharField(max_length=32, unique=True)
    phone_number = models.CharField(max_length=16, unique=True)
    sex = models.CharField(max_length=8, choices=SEX)
    birth_year = models.IntegerField(default=2000)
    birth_month = models.IntegerField(default=1)
    birth_day = models.IntegerField(default=1)
    avatar = models.CharField(max_length=256)  # url
    location = models.CharField(max_length=32)

    # @property 可以把方法的返回值转化为一个只读属性
    
    @cached_property
    def age(self):
        now = datetime.date.today()
        birth_date = datetime.date(
            self.birth_year,
            self.birth_month,
            self.birth_day)
        return (now - birth_date).days // 365
    
    # 手动操作 @cached_property 
    @property
    def profile(self):
        if not hasattr(self, ' _profile'):
            self._profile, is_creat = Profile.objects.get_or_create(id=self.id)
        return self._profile
    
    # 需要重写to_dict()获取age 否则只能得到 birth_year, birth_month, birth_day
    def to_dict(self):
        return {        
            "id":self.id,
            "nick_name":self.nick_name,
            "phone_number":self.phone_number,
            "sex":self.sex,
            "age":self.age,
            "avatar":self.avatar,            
            "location":self.location,
        }


class Profile(models.Model, ModelMixin):
    """
    用户自定义配置
    """

    SEX = (
        ('M', '男'),
        ('F', '女')
    )

    # 定义查找对象条件
    location = models.CharField(max_length=32)
    min_distance = models.IntegerField(default=1)
    max_distance = models.IntegerField(default=10)
    max_data_age = models.IntegerField(default=18)
    min_data_age = models.IntegerField(default=40)
    date_sex = models.CharField(default='M', max_length=8, choices=SEX)

    # 定义软件使用设置
    virbation = models.BooleanField(default=True)
    friend_only = models.BooleanField(default=False)
    auto_play = models.BooleanField(default=True)