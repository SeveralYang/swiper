from random import randrange
from django.core.cache import cache

from swiper import configs
from worker import call_by_worker

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