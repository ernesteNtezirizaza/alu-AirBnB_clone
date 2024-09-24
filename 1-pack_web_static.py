#!/usr/bin/python3
""" Function that compress a folder """
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """The function that compress a folder before sending"""
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        t = datetime.now()
        f = "%Y%m%d%H%M%S"
        archive_path = 'versions/web_static_{}.tgz'.format(t.strftime(f))
        local('tar -cvzf {} web_static'.format(archive_path))
        return archive_path
    except Exception as e:
        print("An error occurred:", e)
        return None
    
