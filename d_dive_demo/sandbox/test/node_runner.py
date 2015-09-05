# -*- coding: utf-8 -*-

from url_generator import URLGenerator
from extract_information import HTMLScraper

class LessonInformation:
    def __init__(self, title, teacher, members):
        self.title = title
        self.teacher = teacher
        self.members = members

if __name__ == '__main__':
    # 今年の年度
    year = 2015

    # 年度＋学科コード＋講義コード（＋クラス）
    lessons = [[year, "G1", "G1001"],
               [year, "G1", "G1002"],
               [year, "G1", "G1003"],
               [year, "G1", "G1004"],
               [year, "G1", "G1041"],
               [year, "G1", "G1046"],
               [year, "G1", "G1060"],
               [year, "G1", "G1064"],
               [year, "G1", "G1071"],
               [year, "G1", "G1072"],
               [year, "G1", "G1068"],
               [year, "G1", "G1082"],
               [year, "G1", "G1083"]
               ]

    # 今年のシラバスのURLを格納するlist
    urls = []
    # 去年のシラバスのURLを格納するlist
    lurls = []
    for lesson in lessons:
        urls.append(URLGenerator(lesson[0], lesson[1], lesson[2]))
        lurls.append(URLGenerator(lesson[0]-1, lesson[1], lesson[2]))

    # 今年のシラバスの情報を抽出するparser
    parsers = []
    # 去年のシラバスの情報を抽出するparser
    lparsers = []

    for url in urls:
        parsers.append(HTMLScraper(url.get_url()))
    for lurl in lurls:
        lparsers.append(HTMLScraper(lurl.get_url()))
        
    # 講義の情報を格納するlist
    lesson_info = []
    for i in range(len(parsers)):
        try:
            lesson_info.append(LessonInformation(parsers[i].get_title(), parsers[i].get_teacher(), lparsers[i].get_members()))
        except:
            print "!!!cannot scrape %s" %urls[i].get_url()
            pass


    # 結果の確認
    for i in range(len(lesson_info)):
        print "講義名 : %s" %lesson_info[i].title
        print "教師名 : %s" %lesson_info[i].teacher
        print "去年の受講者数 : %d" %lesson_info[i].members
        print "潜りやすさ度 : ",
        if lesson_info[i].members < 30:
            print "F(ばれないのは無理でしょう)"
        elif 30 <= lesson_info[i].members < 50:
            print "D(おそらくばれるでしょう)"
        elif 50 <= lesson_info[i].members < 70:
            print "C(おそらく大丈夫でしょう)"
        elif 70 <= lesson_info[i].members < 90:
            print "B(まず問題ないでしょう)"
        else:
            print "A(ばれることはないでしょう)"
        
        print "**********************"
