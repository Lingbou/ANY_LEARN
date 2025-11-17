"""
Gunicorn配置文件
"""

# 服务器套接字
bind = "0.0.0.0:5000"
backlog = 2048

# 工作进程
workers = 4
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

# 重启
max_requests = 1000
max_requests_jitter = 100
preload_app = True

# 日志
accesslog = "-"
errorlog = "-"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# 进程命名
proc_name = 'inventory_api'

# 服务器机制
daemon = False
pidfile = '/tmp/inventory_api.pid'
user = None
group = None
tmp_upload_dir = None

# SSL
keyfile = None
certfile = None

# 监控
statsd_host = None

# 服务器钩子
def on_starting(server):
    """服务器启动时调用"""
    server.log.info("Inventory API Server is starting...")

def when_ready(server):
    """服务器准备就绪时调用"""
    server.log.info("Inventory API Server is ready.")

def worker_int(worker):
    """工作进程收到SIGINT信号时调用"""
    worker.log.info("Worker received INT or QUIT signal")

def pre_fork(server, worker):
    """工作进程fork前调用"""
    server.log.info(f"Worker spawned (pid: {worker.pid})")

def post_fork(server, worker):
    """工作进程fork后调用"""
    server.log.info(f"Worker spawned (pid: {worker.pid})")

def post_worker_init(worker):
    """工作进程初始化后调用"""
    worker.log.info(f"Worker initialized (pid: {worker.pid})")

def worker_exit(server, worker):
    """工作进程退出时调用"""
    server.log.info(f"Worker exiting (pid: {worker.pid})")

def child_exit(server, worker):
    """子进程退出时调用"""
    server.log.info(f"Child worker exited (pid: {worker.pid})")