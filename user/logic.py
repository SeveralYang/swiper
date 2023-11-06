from random import randrange
import requests

from swiper import configs


def generate_random_verify_code(length=6):
    return randrange(10**(length-1), 10**length)


def send_message(phone_number=None, message=None):
    vcode = generate_random_verify_code()
    smscfg = configs.SMS_DATA.copy()
    smscfg['content'] = smscfg['content'] % vcode if message is None else message
    smscfg['mobile'] = phone_number
    print(smscfg)
    response = requests.post(url=configs.SMS_URL, data=smscfg)
    print(response.json())
    return response