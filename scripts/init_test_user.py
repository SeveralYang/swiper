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

for i in range(5000):
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
