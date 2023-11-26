from django.db import models


class Vip(models.Model):
    """VIP表 用于记录所有类别的VIP"""
    name = models.CharField(max_length=32,unique= True)
    level = models.IntegerField()
    price = models.FloatField()

    def has_permission(self,permission_name):
        """检查vip是否具有某种权限"""
        try:
            pid = Permission.objects.get(name = permission_name).id
        except self.model.DoesNotExist:
            return False
        return VipPermission.objects.filter(
            vip_id = self.id,
            permission_id = pid
        ).exists()
    
    def list_permissions(self):
        """查看vip的所有权限"""
        permission_ids = [r.id for r in VipPermission.objects.filter(vip_id = self.id)]
        return Permission.objects.filter(id__in=permission_ids)



class Permission(models.Model):
    """
    权限表 用于记录所有类别的权限
    "vip_flag",                     # 会员标识
    "crazy_permission",             # crazy权限
    "rewind_permission",            # rewind权限
    "any_location",                 # 更改定位
    "unlimited_like",               # 无限喜欢次数
    """
    name = models.CharField(max_length=32,unique= True)


class VipPermission(models.Model):
    """
    会员权限关系表
    用于记录 各种类别的VIP 所拥有的权限
    """
    vip_id = models.IntegerField()
    permission_id = models.IntegerField()