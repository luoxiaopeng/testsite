"""gunicorn WSGI server configuration."""
from multiprocessing import cpu_count
from os import environ

from prometheus_client import multiprocess


def worker_exit(server, worker):
    multiprocess.mark_process_dead(worker.pid)


bind = f'0.0.0.0:956'
workers = cpu_count() * 2
worker_class = 'uvicorn.workers.UvicornWorker'
threads = 0
worker_connections = 0
worker_tmp_dir = '/dev/shm'
timeout = 60
preload = False
max_requests = 90000
max_requests_jitter = 200
