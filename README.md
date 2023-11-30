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

python ./manage.py makemigrations           # 数据库
python ./manage.py migrate     

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
celery -A worker worker -l INFO
```

# redis
```
docker run -d -p 6379:6379 -it redis/redis-stack:latest
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
```
# 如何储存静态文件
1 Nginx 
2 CDN 各地建立镜像站
3 云存储 阿里云 七牛云

# 修改git ignore 
```
git rm -r --cached .
git add .
git commit -m "update .gitignore"
git push 
```

# 实例方法 静态方法 类方法
```
class A:

    def __init__(self) -> None:
        self.x = 1
        self.y = 2

    def f1 (self):
        print(self.x + self.y)
        return self
    
    @classmethod
    def f2(cls):
        print(cls.x + cls.y)
        return cls
    
    @staticmethod
    def f3(self):
        print(self.x + self.y)
        return self


if __name__ == "__main__":
    a = A()

    a == a.foo1()  # True
    
```
# 缓存管理
memcached 只支持字符串
    set:保存一个数据
    get:获取一个数据
    incr:
    decr:
    watch:

reids

# 分布式数据库
```
单台服务器能力上限约为500w条数据
若有500 w *10 条数据 则需要进行数据分片
数据分片
    1分表
        水平拆分
        竖直拆分
    2分库

```

# 压力测试及TCP相关
压力测试工具
    apache benchmark
    siege
    webbench
    wrk
    压力指标: RPS request per second
    apt-get install apache2-utils
    ab -n 1000 -c 10 url
        -n 1000     : 一共发送1000条请求
        -c 10       ：模拟10个用户发送请求

HTTP 协议可以看作是建立在TCP基础上的短连接协议，具有和TCP一样的缺点和优点

    此外由于其属于短链接 在完成一次通信后就会断开
    如需再次通信则需要再次进行三次握手

    三次握手
        第一次 client  ->   SYN                 ->server    
        第二次 client  <-   AXK + SYN           <-server    
        第三次 client  ->   AXK                 ->server    

        客户端和服务器同时属于closed状态，表示没有连接关系。
        客户端发送请求，客户端打开发送(SYN-sent)状态，同时服务器打开监听(Listen)状态；
        服务器在接收到客户端的请求时，服务器切换为回复(SYN-recvd)状态；
        客户端在接收到服务器的响应时，客户端切换为稳定连接(Estab-lished)状态的同时发送第二次数据包。
        服务器在接收到客户端的第二次数据时，服务器切换为稳定连接(Estab-lished)状态。
        双方建立稳定连接后，开始正常通信数据。

进程
    - 资源占用较多 python进程约为35Mb
    - 通信方式, 需要媒介进行通信，如：socket 管道 文件 共享内存通信
    - 多任务切换性能 or 上下文切换 稍慢 不够灵活     

线程
    - 资源占用较少 一般为2Kb
    - 通信方式, 直接通信
    - 多任务切换性能 稍快 不够灵活

# gunicorn

http server 驱动 django 

Request ---> Gunicorn ---->wsgi ---->Django
            |             |         |
            | HTTP_Server | WSGI    |WebAPP


HTTP_Server 用于建立或断开与客户端的连接，发送或接收客户端的数据
 
WSGI : web server gateway interface    
Gunicorn为每个请求创建一个协程 asyncio
wsgi.py 将整个swiper 封装为一个 wsgi 对象 并与Gunicorn对接




# 启动
```
docker run -d -p 6379:6379 -it redis/redis-stack:latest

python manage.py runserver 0.0.0.0:8000
gunicorn -c swiper/gunicorn_config.py swiper.wsgi

celery -A worker worker -l INFO -P eventlet

ab -n 1000 -c 50 127.0.0.1:8000/api/user/get_profile
```

