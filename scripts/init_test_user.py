import os
import sys
import random

import django


BASE_DIR = os.path.dirname( # swiper
    os.path.dirname( # swiper\scripts
        os.path.abspath(__file__) # swiper\scripts\init_test_user.py
    )
)
BACK_END = os.path.join(BASE_DIR,'backend')

sys.path.insert(0,BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE","swiper.settings")
django.setup()


from user.models import User
from vip.models import  *



last_names = (
"赵", "钱", "孙", "李", "周", "吴", "郑", "王",
"冯", "陈", "楮", "卫", "蒋", "沈", "韩", "杨",
"朱", "秦", "尤", "许", "何", "吕", "施", "张",
"孔", "曹", "严", "华", "金", "魏", "陶", "姜",
"戚", "谢", "邹", "喻", "柏", "水", "窦", "章",
"云", "苏", "潘", "葛", "奚", "范", "彭", "郎",
"鲁", "韦", "昌", "马", "苗", "凤", "花", "方",
"俞", "任", "袁", "柳", "酆", "鲍", "史", "唐",
"费", "廉", "岑", "薛", "雷", "贺", "倪", "汤",
"滕", "殷", "罗", "毕", "郝", "邬", "安", "常",
)

first_names = {
    "male":(
        "伟", "超", "勇", "杰",
        "晨", "飞", "宇", "鑫",
    ),
    "female":(
        "琦", "倩", "文", "丽"
        "娟", "艳", "芳", "敏",
        "雅", "雪", "倩", "珊",
    )
}

LOCATIONS = (
"北京","天津", "河北", "山西", "内蒙", "辽宁", "吉林", "黑龙江",
"上海","江苏", "浙江", "安徽", "福建", "江西", "山东", "河南",
"湖北","湖南", "广东", "广西", "海南", "重庆", "四川", "贵州",
"云南","西藏", "陕西", "甘肃", "青海", "宁夏", "新疆", "台湾",
"香港","澳门",
)

def random_name():
    sex = random.choice([ "male", "female"])
    name = f"{random.choice(last_names)}{random.choice(first_names[sex])}"
    return 'M' if sex == 'male' else "F", name

def create_robots(n):
    for i in range(n):
        sex, name = random_name()
        try:
            User.objects.create(
            nick_name = name,
            phone_number =str(random.randrange(21000000000,21900000000)),
            sex = sex,
            birth_year = random.randint(1990,2005),
            birth_month = random.randint(1,12),
            birth_day = random.randint(1,28),
            location = random.choice(LOCATIONS)
            )
            print(f"created User {name}")
        except:
            pass

def init_permissions():
    """
    初始化所有权限表 设定所有应有的权限种类
    """
    permissions = [
    "vip_flag",                     # 会员标识
    "crazy_permission",             # crazy权限
    "rewind_permission",            # rewind权限
    "any_location",                 # 更改定位
    "unlimited_like",               # 无限喜欢次数
    ]
    for p_name in permissions:
        Permission.objects.get_or_create(name=p_name)

def init_vip():
    """初始化vip信息表 规定 Vip相关信息 如名称 等级 价格"""
    for i in range(4):
        Vip.objects.get_or_create(
            name = f"会员{i}", 
            level = i,
            price = i * 5,
        )

def init_vip_permission():
    """
    初始化VIP和权限关系表 即规定各个等级的VIP分别具有哪些权限
    """
    vip1 = Vip.objects.get(level=1)
    vip2 = Vip.objects.get(level=2)
    vip3 = Vip.objects.get(level=3)

    vip_flag = Permission.objects.get(name = "vip_flag") 
    crazy_permission = Permission.objects.get(name = "crazy_permission") 
    rewind_permission = Permission.objects.get(name = "rewind_permission") 
    any_location = Permission.objects.get(name = "any_location") 
    unlimited_like = Permission.objects.get(name = "unlimited_like") 

    # vip1 权限
    VipPermission.objects.get_or_create(vip_id = vip1.id,permission_id = vip_flag.id)
    VipPermission.objects.get_or_create(vip_id = vip1.id,permission_id = crazy_permission.id)
    # vip2 权限
    VipPermission.objects.get_or_create(vip_id = vip2.id,permission_id = vip_flag.id)
    VipPermission.objects.get_or_create(vip_id = vip2.id,permission_id = crazy_permission.id)
    VipPermission.objects.get_or_create(vip_id = vip2.id,permission_id = rewind_permission.id)
    # vip3 权限
    VipPermission.objects.get_or_create(vip_id = vip3.id,permission_id = vip_flag.id)
    VipPermission.objects.get_or_create(vip_id = vip3.id,permission_id = crazy_permission.id)
    VipPermission.objects.get_or_create(vip_id = vip3.id,permission_id = rewind_permission.id)
    VipPermission.objects.get_or_create(vip_id = vip3.id,permission_id = any_location.id)
    VipPermission.objects.get_or_create(vip_id = vip3.id,permission_id = unlimited_like.id)

if __name__ == "__main__":
    create_robots(2000)
    init_permissions()
    init_vip()
    init_vip_permission()