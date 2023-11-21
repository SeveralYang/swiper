import json

from django.http import HttpResponse


def render_json(data,code=0):
    res  = {
    "code":code,
    "data":data
    }
    return HttpResponse(json.dumps(res,separators=[',',':']))


if __name__ == "__main__":

    a = render_json(
        {"user":123,"phone":456}
        )
    print(a)