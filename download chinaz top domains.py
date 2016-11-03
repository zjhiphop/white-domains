# -*- coding:utf-8 -*-
__author__ = 'tianjianbo@126.com'
import urllib2
from bs4 import BeautifulSoup
import threading
import Queue


class DownloadThread(threading.Thread):
    def __init__(self, que, mutex, file):
        threading.Thread.__init__(self)  # important
        self.que = que
        self.mutex = mutex
        self.file = file

    def run(self):
        while not self.que.empty():
            url = self.que.get()
            try:
                request = urllib2.Request(url)
                response = urllib2.urlopen(request)
            except Exception, e:
                self.que.put(url)
                print 'a Thread GG'
                continue
            soup = BeautifulSoup(response, "html.parser")
            tag_list = soup.find_all("span", class_="col-gray")
            self.mutex.acquire(1)
            for i in range(1, len(tag_list)):
                self.file.write(tag_list[i].string + '\n')
            self.mutex.release()


def load_url_set():
    url_begin = 'http://top.chinaz.com/all/index.html'
    url_base = 'http://top.chinaz.com/all/index_'
    queue = Queue.Queue()
    queue.put(url_begin)
    for i in range(2, 1761, 1):
        url_now = url_base + str(i) + '.html'
        queue.put(url_now)
    return queue


def main():
    fw = open('result/chinaz_top_domains.txt', 'w')
    thread_num = 20
    my_queue = load_url_set()
    result = Queue.Queue()
    mutex = threading.Lock()
    for i in range(thread_num):
        download_thread = DownloadThread(my_queue, mutex, fw)
        download_thread.start()
    while threading.activeCount() > 1:
        pass
    else:
        print "All done!"
        fw.close()


if __name__ == '__main__':
    main()