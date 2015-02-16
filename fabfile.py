# -*- coding:utf-8 -*-

import os
from fabric.api import run, env, cd, sudo
env.hosts = ['128.199.232.167']

env.user = os.environ['PRODUCTION_USER_NAME']
env.password = os.environ['PRODUCTION_PASSWORD']
env.port = 22


def pull():
    with cd('/home/bustta/myWebApps/PttNotifier'):
        run('git pull')


def restartNginx():
    sudo('service nginx restart')


def collectStatic():
    path = "/home/bustta/myWebApps"
    with cd('/home/bustta/myWebApps/PttNotifier'):
        run('. %s/venv/pttnotifier/bin/activate && python manage.py collectstatic --noinput ' % path)
