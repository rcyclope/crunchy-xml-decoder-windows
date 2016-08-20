import os, re, urllib2, sys
from collections import deque

print 'indicate the url : '
url=raw_input()
mykey = urllib2.urlopen(url)
take = open("queue_.txt", "w")

for text in mykey:
    match = re.search('<a href="/(.+?)" title=', text)
    if match:
        print >> take, 'http://www.crunchyroll.com/'+match.group(1)

take.close()
	
with open('queue_.txt') as f,  open('queue.txt', 'w') as fout:
    fout.writelines(reversed(f.readlines()))

os.remove('queue_.txt')
