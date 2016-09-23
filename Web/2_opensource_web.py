# -*- coding: utf-8 -*-
import Queue
import threading
import os
import urllib2

threads = 10

target = "http://www.test.com"
#target = "http://electrical3345678.ddns.net/demo/ps_salon/"
directory = "/Users/justin/Downloads/joomla-3.1.1"
filters = [".jpg", ".gif", "png", ".css"]

# os.chdir(directory)

web_paths = Queue.Queue()
#os.walk , 用來搜索某目録下的所有檔案, 下列為本目録, r ,d ,f 分別為dirPath, dirNames, fileNames
for r, d, f in os.walk("."):
    for files in f:
        remote_path = "%s/%s" % (r, files)
        print (remote_path)
        if remote_path.startswith("."): #確認有 點的 話 則為true
            remote_path = remote_path[1:]
        if os.path.splitext(files)[1] not in filters:
            web_paths.put(remote_path)
            #print (web_paths.get())


def test_remote():
    while not web_paths.empty():
        path = web_paths.get()
        url = "%s%s" % (target, path)

        request = urllib2.Request(url)

        try:
            response = urllib2.urlopen(request)
            content = response.read()

            print "[%d] => %s" % (response.code, path)

            response.close()

        except urllib2.HTTPError as error:
            # print "Failed %s" % error.code
            pass


for i in range(threads):
    print "Spawning thread: %d" % i
    t = threading.Thread(target=test_remote)
    t.start()
