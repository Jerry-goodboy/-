#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from subprocess import call
import sys, os
import multiprocessing

num_threads = 10


class RenderThread:
    def __init__(self, q):
        self.q = q
    
    def render_tile(self, pic_url):
        os.system("wget -t 2 "+pic_url)
    
    
    def loop(self):
        
        
        while True:
            #Fetch a tile from the queue and render it
            r = self.q.get()
            if (r == None):
                self.q.task_done()
                break
            else:
                (pic_url) = r
            
            
            self.render_tile(pic_url)
            
            self.q.task_done()


if __name__ == "__main__":
    queue = multiprocessing.JoinableQueue(32)
    renderers = {}
    for i in range(num_threads):
        renderer = RenderThread(queue)
        render_thread = multiprocessing.Process(target=renderer.loop)
        render_thread.start()
        #print "Started render thread %s" % render_thread.getName()
        renderers[i] = render_thread
        
    fp = open("output.txt")
    for i in fp.readlines():
        # print i
        if i.startswith("error"):
            continue
        if not i.startswith("http"):
            # print "http://www.qiubaichengnian.com/"+i
            queue.put("http://www.qiubaichengnian.com/"+i)
    
        queue.put(i)

    for i in range(num_threads):
        queue.put(None)
        # wait for pending rendering jobs to complete
        queue.join()
        for i in range(num_threads):
            renderers[i].join()
