#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

def notice(msg, title = "notice"):
    os.system('osascript -e \'display notification "%s" with title "%s"\'' % (msg, title))
