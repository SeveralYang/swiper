import json

from django.http import HttpResponse
from django.conf import settings

def render_json(data,code=0):
    res  = {
    "code":code,
    "data":data
    }
    if settings.DEBUG :
        res =json.dumps(res,ensure_ascii=False,indent=4,sort_keys=True)
    else:
        res =json.dumps(res,ensure_ascii=False,separators=[',',':'])
    return  HttpResponse(res)


if __name__ == "__main__":

    a = render_json(
        {"user":123,"phone":456}
        )
    print(a)