#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import time
from workflow import Workflow3

from clipboard import get_paste_img_file
from upload import upload_qiniu
import util


def main(wf):
    img_file, need_format, ext_format = get_paste_img_file()
    url = os.getenv('qiniu_domain_url')
    bulk = os.getenv('bulk')
    if img_file:
        # 有图片，生成一个唯一的图片名
        upload_name = "%s.%s" % (int(time.time() * 1000), ext_format)
        if need_format:
            markdown_url = 'http://%s/%s/%s' % (url, bulk,  upload_name)
        else:
            markdown_url = 'http://%s/%s/%s' % (url, bulk, upload_name)




        if not upload_qiniu(img_file.name, upload_name):
            util.notice("上传失败")
        else:
        # 复制到剪切板栗
        # os.system("echo '%s' | pbcopy" % markdown_url)


        # wf.add_item(u'上传截图', u'成功！')
        # wf.send_feedback()
            print markdown_url
    else:
        util.notice('剪切板中没有图片')


if __name__ == '__main__':
    wf = Workflow3()
    sys.exit(wf.run(main))
