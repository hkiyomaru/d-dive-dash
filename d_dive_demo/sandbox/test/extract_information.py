# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from html_getter import HTMLGetter

'''
argument: html data
return: unicode data
'''

class HTMLScraper:
    def __init__(self, url):
        html = HTMLGetter(url)
        page = html.get_page_text()
        self.soup = BeautifulSoup(page, 'lxml')

    # 講義名を取得
    def get_title(self):
        return unicode(self.soup.body.find_all('b')[2].string)[1:].encode('utf-8')

    # 教師名を取得
    def get_teacher(self):
        return unicode(self.soup.body.find_all('a')[0].string)[1:-1].encode('utf-8')

    # 講義概要を取得
    def get_overview(self):
        return unicode(self.soup.body.find_all('p')[4].string).encode('utf-8')

    # 各講義の内容を取得
    def get_lessons(self):
        lesson_list=[]
        for i in range(3,48,3):
            lesson_list.append(unicode(self.soup.body.find_all('td', valign="top")[i].string)[1:-1].encode('utf-8'))
        return lesson_list

    # 去年の受講者数を取得
    def get_members(self):
        return int(self.soup.find_all('table')[7].find_all('td')[0].string)
        
'''
動作デバッグ用main関数
'''
if __name__ == '__main__':
    parser = HTMLScraper('https://syllabus.doshisha.ac.jp/html/2014/G1/1G1003000.html')
    print parser.get_overview()
