# -*- coding: utf-8 -*-
import os
from qiniu import Auth, put_file
import util

def upload_qiniu(path, upload_name):
    ''' 上传文件到七牛 '''
    ak = os.getenv('access_key')
    sk = os.getenv('secret_key')
    bulk = os.getenv('bulk')
    qiniu_domain_url = os.getenv('qiniu_domain_url')

    if ak == None or sk == None:
        util.notice("请输入七牛相关配置")
        return False
    q = Auth(ak, sk)
    key = '%s/%s' % (bulk, upload_name)

    token = q.upload_token(bulk, key)
    ret, info = put_file(token, key, path)
    return ret != None and ret['key'] == key
