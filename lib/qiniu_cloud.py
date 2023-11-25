from qiniu import Auth, put_file, etag
from swiper import configs
from worker import call_by_worker


def upload_to_QINIU(localfile,key):
    """ 
    Args:
        localfile 本地文件路径
        key 云文件名
    """
    q = Auth(configs.QINIU_AK, configs.QINIU_SK)
    bucket = configs.QINIU_BUCKET_NAME
    token = q.upload_token(bucket=bucket,key=key,expires=3600)
    ret, info = put_file(token, key, localfile, version='v2') 
    # print(ret,info)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)
    return info.status_code == 200

#手动装饰 定义 异步上传
async_upload_to_QINIU = call_by_worker(upload_to_QINIU)