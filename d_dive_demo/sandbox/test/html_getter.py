# -*- coding: utf-8 -*-

import urllib
import urllib2
import sys

'''
argument: url, (values), (headers)
return: html
'''

class HTMLGetter:
    def __init__(self, url, values={}, headers={}):
        self.url = url
        self.values = values
        self.headers = headers

    def get_page_text(self):
        data = urllib.urlencode(self.values)
        request = urllib2.Request(self.url, data, self.headers)
        response = urllib2.urlopen(request)
        try:
            return response.read()
        except URLError, e:
            if hasattr(e, 'reason'):
                print 'We failed to reach a server.'
                print 'Reason: ', e.reason
            elif hasattr(e, 'code'):
                print 'The server couldn\'t fulfill the request.'
                print 'Error code: ', e.code

'''
動作デバッグ用main関数
'''
if __name__ == '__main__':
    html = HTMLGetter('https://syllabus.doshisha.ac.jp/html/2014/G1/1G1003000.html')
    print html.get_page_text()
