# -*- coding: utf-8 -*-

'''
シラバスのURLの例
https://syllabus.doshisha.ac.jp/html/2014/G1/1G1028000.html
'''
class URLGenerator:
    def __init__(self, year, department, classcode, classroom="000"):
        self.URL = "https://syllabus.doshisha.ac.jp/html/" + str(year) + "/" + str(department) + "/1"  + str(classcode) + str(classroom) + ".html"
    # 引数情報から作成されたURLを返す
    def get_url(self):
        return self.URL

'''
動作デバッグ用main関数
'''
if __name__ == '__main__':
   url = URLGenerator(2015, "G1", "G1028")
   print url.get_url()
