import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["제목", "내용", "날짜", "링크"])

a = input("몇번 글 부터 크롤링을 시작하시겠습니까?")
a = int(a)
b = input("몇 개를 크롤링 하시겠습니까?")
b = int(b)
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
params = {'id': 'government'}
searchList = []


for i in tqdm(range(0,b)) :
    a = a - 1
    
    BASE_URL = "https://gall.dcinside.com/board/view/?id=government&no="+str(a)+"&_rk=eYK&page=1"
    resp = requests.get(BASE_URL, params=params, headers=headers)
    try : 
        soup = BeautifulSoup(resp.content, 'html.parser')
        contents = soup.find("div", attrs={"class":"view_content_wrap"})
    

        print('-'*15)

        # 제목ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        title = contents.find("span", attrs={"class":"title_subject"})
        print("제목: ", title.text)

        # 내용ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        write = contents.find('div', class_='writing_view_box')
        print("내용: ", write.text.strip())

        #날짜ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        data_tag = contents.find('span', class_='gall_date')
        date_dict = data_tag.attrs
        
        if len(date_dict) is 2:
            print("날짜:", date_dict['title'])
        else:
            print("날짜:", data_tag.text)
            pass

        #링크ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        link = BASE_URL
        print("링크: ", link)

    except :
        print("게시글이 삭제되었습니다.")
        pass

    sheet.append([title.text, write.text, date_dict['title'], link])
wb.save("dc_.xlsx")