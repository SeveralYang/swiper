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
./manage.py makemigrations           # 
```
# git 

```
git add .  
git commit -m 'init'  
git push  
```

