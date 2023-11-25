import os
from urllib.parse import urljoin

from random import randrange
from django.core.cache import cache
from django.conf import settings

from swiper import configs
from worker import call_by_worker
from lib.qiniu_cloud import async_upload_to_QINIU

def generate_random_verify_code(length=6):
    return randrange(10**(length-1), 10**length)

@call_by_worker
def send_message(phone_number=None, message=None):
    """异步发送验证码"""
    vcode = generate_random_verify_code()
    key = f"vcode_{phone_number}"
    cache.set(key=key, value=vcode, timeout=60*3)
    smscfg = configs.SMS_DATA.copy()
    smscfg['content'] = smscfg['content'] % vcode if message is None else message
    smscfg['mobile'] = phone_number
    response =None # requests.post(url=configs.SMS_URL, data=smscfg)
    print(f'your number is {phone_number}, your code is {vcode}')
    return response

@call_by_worker
def check_vcode(phone_number=None, post_code=None):
    """检查验证码是否正确"""
    key = f"vcode_{phone_number}"
    saved_code = cache.get(key) 
    return  saved_code == post_code

def write_file(file,user,index=0,mode='wb'):
    filename = f"Avatar-{user.id}-{index}{os.path.splitext(str(file))[-1]}"
    path = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT, filename)
    with open(path,mode) as new_file:
        for trunck in file.chunks():
            new_file.write(trunck)
    new_file.close()
    async_upload_to_QINIU(path,filename)
    user.avatar = urljoin(configs.QINIU_URL, filename)
    user.save()
    return user.avatar
