#!/usr/bin/python3
import binascii
import sys
import time
import re
import os

displaylabel=""

masterfilter_restrict=[
    ]

masterfilter_exclude=[
    ]

def execute(filename, backupfiledata, modifyggpk):
    filedata, encoding, bom = modifyggpk.stringcleanup(backupfiledata, "UTF-16-LE")
    filedatamod=re.sub(r'"shadows_enabled": true,', r'"shadows_enabled": false,', filedata)
    filedatamod=re.sub(r'"use_forced_screenspace_shadows": true,', r'"use_forced_screenspace_shadows": false,', filedatamod)
    return filedatamod, encoding, bom
