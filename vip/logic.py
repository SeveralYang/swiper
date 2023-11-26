from common import err
from lib.http import render_json

def permission_required(need_perm):
    """权限检查装饰器"""
    def decorate(view_function):
        """ view_function 为装饰器所装饰的函数"""
        def warp(request):
            """ request 为 所装饰的函数的参数, 此处所装饰的函数固定为 request """
            user = request.user
            if user.vip.has_permission(need_perm):
                response = view_function(request)
                return response
            else:
                return render_json(data=None,code=err.NOT_HAS_PERMISSION)
        return warp
    return decorate