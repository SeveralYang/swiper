from qiniu import Auth, put_file, etag
from swiper import configs

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
    print(ret,info)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)

if __name__ == "__main__":
    upload_to_QINIU("D:\code\swiper\lib\__init__.py",'hell.py')