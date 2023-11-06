from user.logic import send_message




def get_vertify_code(request):
    """手机注册"""
    moblie = request.get("moblie")
    send_message(moblie)

def login(request):
    pass


def get_profile(request):
    pass


def modified(request):
    pass


def upload_avator(request):
    pass

def test():
    send_message('123')