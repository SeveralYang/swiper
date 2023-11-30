from multiprocessing import cpu_count

# 一般绑定在内网环境
bind = ["127.0.0.1:8000"]
daemon = False #是否后台运行 守护进程
pidfile = 'logs/gunicorn.pid'

workers = cpu_count() * 2
worker_class = "gevent"
worker_connections =  65535


keepalive = 60 # 保持时间 避免频繁的三次握手
timeout = 30 # 请求超时时间
graceful_timeout = 10 
forwarded_allow_ips = '*' # 允许访问源

# log
capture_output = True
loglevel  = 'info'
errorlog = 'logs/gunicorn.log'