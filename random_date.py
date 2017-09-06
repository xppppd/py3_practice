# 为正则表达式练习创建随机数据，将生成的数据输出到屏幕
from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')
f = open('/Users/xiongpan/Desktop/1.txt', 'w')
for i in range(randrange(5, 11)):
    dtint = randrange(maxsize)
    dtstr = ctime(dtint / 10000000000)
    llen = randrange(4, 8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for i in range(dlen))
    f.write('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen) + '\n')
    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen))
f.close()
