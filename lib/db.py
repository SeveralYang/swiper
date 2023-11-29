from django.db import models
from django.core.cache import cache

# from lib.cache import rds

@classmethod
def get(cls,*args,**kwargs):
    """
    优先从缓存库中获取数据, 如果缓存中不存在数据则从数据库中获取并存入缓存
    """
    pk = kwargs.get('pk') or kwargs.get('id')
    
    # 从cache获取
    if pk is not None:
        key = f"Model_{cls.__name__}_{pk}"
        model_obj = cache.get(key)
        if isinstance(model_obj,cls):
            return model_obj
    
    # cache中不存在 则从数据库获取
    model_obj = cls.objects.get(*args,**kwargs)
    key = f"Model_{cls.__name__}_{model_obj.pk}"
    cache.set(key,model_obj)

@classmethod
def get_or_creat(cls,*args,**kwargs):
    
    pk = kwargs.get('pk') or kwargs.get('id')
    
    # 从cache获取
    if pk is not None:
        key = f"Model_{cls.__name__}_{pk}"
        model_obj = cache.get(key)
        if isinstance(model_obj,cls):
            return model_obj, False
        
    # cache中不存在 则创建
    model_obj, created = cls.objects.get_or_created(*args,**kwargs)
    key = f"Model_{cls.__name__}_{model_obj.pk}"
    cache.set(key,model_obj)
    return model_obj, True

def save(self,force_insert=False, force_update=False, using=None, update_fields=None):
    # self._ori_save 为 models.Model.save() 经替换所得
    self._ori_save(force_insert,force_update,using,update_fields)
    key = f"Model_{self.__class__.__name__}{self.pk}"
    cache.set(key,self)


def to_dict(self,*ignore):
    attr_dict = {}
    for field in self._meta.fields:
        if field.name in ignore:
            continue
        attr_dict[field.name] = getattr(self,field.name)
    return attr_dict


def patch_model():
    """
    动态更新Django的Model,添加我们所期望的实现的功能
    因为Model 在Django中是一个较为特殊的类,如果通过继承的方法增加or修改原有方法,Django会将继承的类视作
    app.models, 所以只能通过 monkey patch 方法动态修改来实现动态增加功能
    注意 本方法需要在django init 时调用才能在各个模块直接使用 
    """
    models.Model.get = get
    models.Model.get_or_create = get_or_creat

    # 将models.Model.save() 复制到 models.Model._ori_save()
    # 使用自定义save()替换 models.Model.save()
    models.Model._ori_save = models.Model.save
    models.Model.save = save

    models.Model.to_dict = to_dict