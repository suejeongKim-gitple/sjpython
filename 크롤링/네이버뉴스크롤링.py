# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from datetime import datetime #크롤링 결과 엑셀 저장시 저장하는 시간을 엑셀 이름으로 설정하기 위해 필요.
import requests #웹크롤링을 위한 모듈
import pandas as pd 
import re #정규표현식 날짜와 내용 요약의 정제화 작업을 위해 필요
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
< naver 뉴스 검색시 리스트 크롤링하는 프로그램 > _select사용
- 크롤링 해오는 것 : 링크,제목,신문사,날짜,내용요약본
- 날짜,내용요약본  -> 정제 작업 필요
- 리스트 -> 딕셔너리 -> df -> 엑셀로 저장 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#각 크롤링 결과 저장하기 위한 리스트 선언 
title_text=[]
link_text=[]
source_text=[]
date_text=[]
contents_text=[]
result={}

#엑셀로 저장하기 위한 변수
RESULT_PATH ='C:/Users/ksjsj/OneDrive/바탕 화면/pythonworkspace/sjpython/크롤링' #결과 저장할 경로
now = datetime.now() #파일이름 현 시간으로 저장하기

#날짜 정제화 함수
def date_cleansing(test):
    try:
        #지난 뉴스
        #머니투데이  10면1단  2018.11.05.  네이버뉴스   보내기  
        pattern = '\d+.(\d+).(\d+).'  #정규표현식 
    
        r = re.compile(pattern)
        match = r.search(test).group(0)  # 2018.11.05.
        date_text.append(match)
        
    except AttributeError:
        #최근 뉴스
        #이데일리  1시간 전  네이버뉴스   보내기  
        pattern = '\w* (\d\w*)'     #정규표현식 
        
        r = re.compile(pattern)
        match = r.search(test).group(1)
        #print(match)
        date_text.append(match)


#내용 정제화 함수 
def contents_cleansing(contents):
    first_cleansing_contents = re.sub('<dl>.*?</a> </div> </dd> <dd>', '', 
                                      str(contents)).strip()  #앞에 필요없는 부분 제거
    second_cleansing_contents = re.sub('<ul class="relation_lst">.*?</dd>', '', 
                                       first_cleansing_contents).strip()#뒤에 필요없는 부분 제거 (새끼 기사)
    third_cleansing_contents = re.sub('<.+?>', '', second_cleansing_contents).strip()
    contents_text.append(third_cleansing_contents)
    #print(contents_text)
    

def crawler(maxpage,query,sort,s_date,e_date): #def=> 함수를 정의해줄게

    # s_from = s_date.replace(".","")
    # e_to = e_date.replace(".","")
    page = 1  
    maxpage_t =(int(maxpage)-1)*10+1   # 11= 2페이지 21=3페이지 31=4페이지  ...81=9페이지 , 91=10페이지, 101=11페이지 #int는 숫자나 문자열을 정수형으로 변환
    
    while page <= maxpage_t:
        # url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort="+sort+"&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)
        url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort="+sort+"&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + "%2Ca%3A&start=" + str(page)
        
        response = requests.get(url)
        html = response.text
 
        #뷰티풀소프의 인자값 지정
        soup = BeautifulSoup(html, 'html.parser')

    #     news_list = soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')
    #     for news in news_list:
    #         #<a>태그에서 제목과 링크주소 추출
    #         atag = news.select_one("div.news_wrap.api_ani_send > div > a")            
    #         title_text.append(atag["title"])
    #         link_text.append(atag["href"])
    #         #신문사 추출
    #         source = news.select_one("div.news_wrap.api_ani_send > div > div.news_info > div > a.info.press")    
    #         source_text.append(source.text)

    #         #날짜 추출
    #         # date = news.select_one("div.news_wrap.api_ani_send > div > div.news_info > div > span")      
    #         # date_cleansing(date.text)  #날짜 정제 함수사용
    #         #본문요약본
    #         content = news.select_one("div.news_wrap.api_ani_send > div > div.news_dsc > div > a")
    #         contents_cleansing(content) #본문요약 정제화
    # result= {"date" : date_text , "title":title_text ,  "source" : source_text ,"contents": contents_text ,"link":link_text }

 
        #<a>태그에서 제목과 링크주소 추출
        atags = soup.select('news_tit')
        for atag in atags:
            title_text.append(atag.text)     #제목
            link_text.append(atag['href'])   #링크주소

        #신문사 추출
        source_lists = soup.select('info press')
        for source_list in source_lists:
            source_text.append(source_list.text)    #신문사
        
        #날짜 추출 
        date_lists = soup.select('info')
        for date_list in date_lists:
            test=date_list.text   
            date_cleansing(test)  #날짜 정제 함수사용 
        
        #본문요약본
        contents_lists = soup.select('api_txt_lines dsc_txt_wrap')
        for contents_list in contents_lists:
            #print('==='*40)
            #print(contents_list)
            contents_cleansing(contents_list) #본문요약 정제화
        
        
        #모든 리스트 딕셔너리형태로 저장
        result= {"date" : date_text , "title":title_text ,  "source" : source_text ,"contents": contents_text ,"link":link_text }  
        print(page)
        
        df = pd.DataFrame(result)  #df로 변환
        page += 10

        outputFileName = '%s-%s-%s  %s시 %s분 %s초 merging.xlsx' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
        df.to_csv(RESULT_PATH+outputFileName,sheet_name='sheet1', encoding='utf-8')

    
    # 새로 만들 파일이름 지정
    # outputFileName = '%s-%s-%s  %s시 %s분 %s초 merging.xlsx' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
    # df.to_excel(RESULT_PATH+outputFileName,sheet_name='sheet1')
    
    
def main():
    info_main = input("="*50+"\n"+"입력 형식에 맞게 입력해주세요."+"\n"+" 시작하시려면 Enter를 눌러주세요."+"\n"+"="*50) #\n은 줄바꿈
    maxpage = input("최대 크롤링할 페이지 수 입력하시오: ")  
    query = input("검색어 입력: ")  
    sort = input("뉴스 검색 방식 입력(관련도순=0  최신순=1  오래된순=2): ")    #관련도순=0  최신순=1  오래된순=2
    s_date = input("시작날짜 입력(2019.01.04):")  #2019.01.04
    e_date = input("끝날짜 입력(2019.01.05):")   #2019.01.05
    
    crawler(maxpage,query,sort,s_date,e_date) 
    
main()

#보고 해석해볼것 https://bumcrush.tistory.com/116


#     '''
#     df 랑 상관없이
# result= {"date" : date_text , "title":title_text ,  "source" : source_text ,"contents": contents_text ,"link":link_text }
# 이게 값이 비어있어요
# 웹 페이지 자체에서 추출하는 로직이 안맞는듯 한데
# 최초 https://search.naver.com/search.naver?where=news&query=챗봇&sort=0&ds=2021.01.29&de=202[…]01.29&nso=so%3Ar%2Cp%3Afrom20210129to20210129%2Ca%3A&start=1 검색 url 이 이건데
# 첫번째 for 문에서
# #<a>태그에서 제목과 링크주소 추출
#         atags = soup.select('._sp_each_title')
#         for atag in atags:
#             title_text.append(atag.text)     #제목
#             link_text.append(atag['href'])   #링크주소
#         print(page, title_text, link_text)
# print 문 추가했는데
# 값이 다 비어있어요
# 즉, 제목 추출하는 부분이 잘 못 되었을듯
# 네이버 검색 결과 페이지 형태가 바뀌었을 확률이;
# atags = soup.select('._sp_each_title')
# select 가 바뀌었으니 여기서부터 다시 분석~
#     '''

# news_list = soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')
#         for news in news_list:
#             #<a>태그에서 제목과 링크주소 추출
#             atag = news.select_one("div.news_wrap.api_ani_send > div > a")            
#             title_text.append(atag["title"])
#             link_text.append(atag["href"])
#             #신문사 추출
#             source = news.select_one("div.news_wrap.api_ani_send > div > div.news_info > div > a.info.press")    
#             source_text.append(source.text)
#             #날짜 추출
#             # date = news.select_one("div.news_wrap.api_ani_send > div > div.news_info > div > span")      
#             # date_cleansing(date.text)  #날짜 정제 함수사용
#             #본문요약본
#             content = news.select_one("div.news_wrap.api_ani_send > div > div.news_dsc > div > a")
#             contents_cleansing(content) #본문요약 정제화
#result= {"date" : date_text , "title":title_text ,  "source" : source_text ,"contents": contents_text ,"link":link_text } 여기서 date는 빼거나, 그냥 날짜 정제 안하고 그대로 값을 넣어야할듯