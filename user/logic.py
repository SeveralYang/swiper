from random import randrange
import requests
from django.core.cache import cache

from swiper import configs
from worker import call_by_worker

def generate_random_verify_code(length=6):
    return randrange(10**(length-1), 10**length)

@call_by_worker
def send_message(phone_number=None, message=None):
    vcode = generate_random_verify_code()
    cache.set(key=f"vcode_{phone_number}", value=vcode, timeout=60*3) 
    smscfg = configs.SMS_DATA.copy()
    smscfg['content'] = smscfg['content'] % vcode if message is None else message
    smscfg['mobile'] = phone_number
    response = None # requests.post(url=configs.SMS_URL, data=smscfg)
    return response