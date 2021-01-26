import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") #엑셀파일을 열때 한글이 깨지면 utf-8-sig
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t") 
# \t 문자열 사이에 탭 간격을 줄 때 사용
# split함수는 문자열을 공백 혹은 어떠한 기준으로 나눌때 사용하는 함수이다. 
# [ "N", "종목명", "현재가", ...]
print(type(title))
writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: #의미없는 데이터 스킵
            continue
        data = [column.get_text().strip() for column in columns] #strip()은 문자열에서 양쪽에 있는 연속된 모든 공백을 삭제합니다.
        print(data)
        # writer.writerow(data)


    