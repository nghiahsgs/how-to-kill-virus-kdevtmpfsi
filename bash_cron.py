import os
import io
import re
import time
from typing import DefaultDict
def regex_one_value(pattern, input_str):
    regex1=re.compile(pattern)
    kq=regex1.search(input_str)
    if kq:
        kq=kq.group(1)
    else:
        kq=''
    return kq

def read_file(file_name):
    f = io.open(file_name, 'r', encoding='utf-8')
    ndung=f.read()
    f.close()
    return ndung

def replace_space(ndung):
    ndung = ndung.replace("    "," ")
    ndung = ndung.replace("   "," ")
    ndung = ndung.replace("  "," ")
    return ndung
while True:
    # username = 'www-data'
    username = 'apache'
    os.system("ps -aux | grep kdevtmpfsi >a.txt")
    ndung = read_file('a.txt')
    ndung = replace_space(ndung)
    id_process = regex_one_value('%s ([0-9]+) '%username,ndung)
    os.system('kill -9 %s'%id_process)

    os.system("ps -aux | grep kinsing >a.txt")
    ndung = read_file('a.txt')
    ndung = replace_space(ndung)
    id_process = regex_one_value('%s ([0-9]+) '%username,ndung)
    os.system('kill -9 %s'%id_process)

    os.system("ps -aux | grep kthreaddi >a.txt")
    ndung = read_file('a.txt')
    ndung = replace_space(ndung)
    id_process = regex_one_value('%s ([0-9]+) '%username,ndung)
    os.system('kill -9 %s'%id_process)

    # xoa het cac file do virus sinh ra
    os.system("rm -rf /tmp/kdevtmpfsi*")
    os.system("rm -rf /tmp/kinsing*")
    
    time.sleep(15*60) #sleep 30p

