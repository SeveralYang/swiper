# init
```
install conda 
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda 
conda config --set show_channel_urls yes
conda config --show channels
```
```
python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip  
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple  
pip install django==1.11.15 redis gunicorn gevent ipython celery  
pip freeze > requirements 
```
# django
```
django-admin startproject swiper ./  # 新建项目
./manage.py startapp user            # 新建user功能

./manage.py makemigrations           # 数据库
./manage.py migrate     

./manage.py shell                    # 调试
```
# git 

```
git add .  
git commit -m 'init'  
git push  
```

# celery
```
异步任务 Async task  & 定时任务 Celery Beat 
>> 中间件 Broker
>> 执行单元 Celery worker
>> 结果储存 Backend


proj_name/__init__.py
    /celery.py
    /tasks.py

celery -A proj_name worker -l INFO
```

# redis
```
docker run -d -p 6379:6379 -it redis/redis-stack:latest
celery -A worker worker -l INFO
```

# restful
```
restful 是一种网络软件设计的风格 仅适用于与http
URL定位一个网络资源

HTTP
    POST        新建 提交
    GET         获取
    PUT         修改
    DELETE      删除
    HEAD        只获取头部信息
    OPTIONS     查看支持哪些协议 如POST GET
    PATH        部分修改

http状态码
    2.. 成功
    3.. 重定向
    4.. 客户端错误
    5.. 服务端错误

接口格式
{
    "code":200,
    "data":{
        
    }
}


```

# User 所需实现的接口/功能 
```
1 提交手机号
Description : submit your phone number to login  
Method : POST  
Path : /user/verify 
Parameters:
    Field       Reqeired    Type    Description  
    moblie      true        str     用户的手机号
Return `{'code':0, 'data':null}`

2 
```
