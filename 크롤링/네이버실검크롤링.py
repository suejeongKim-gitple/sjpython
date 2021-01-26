import requests
from bs4 import BeautifulSoup 
from datetime import datetime 

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
url = "https://datalab.naver.com/keyword/realtimeList.naver?age=all"
response = requests.get(url, headers=headers) 
soup = BeautifulSoup(response.text, 'lxml')
rank = 1

results = soup. findAll('span','item_title')

search_rank_file = open('naver_rankresult.txt','w', encoding='UTF-8')

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    #파일 출력의 결과는 이걸로 해줘.
    search_rank_file.write(str(rank)+"위:"+result.get_text()+'\n')
    
    # print(result.get_text(), "\n") #\n 줄바꿈 #실검에서 text만 출력
    print(rank,"위:", result.get_text(),'\n')
    rank += 1

    
