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

celery -A worker worker
```

# redis
```docker run -d -p 6379:6379 -it redis/redis-stack:latest```