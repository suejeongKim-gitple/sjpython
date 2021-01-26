import requests
from bs4 import BeautifulSoup #(bs4가 모듈이고 beautifulsoup가 모듈 안 기능임)
from datetime import datetime #오늘 날짜를 프린트하고 싶을때 사용하는 모듈

url = "https://www.daum.net"
response = requests.get(url)  #리퀘스트 잘 깔렸슨지 확인하기
# print(response.text[:500]) #([:500] = 500개까지만 가져와)

# print(type(BeautifulSoup(response.text, 'html.parser')))

soup = BeautifulSoup(response.text, 'lxml')
rank = 1 #순위를 달기 위한 함수 
#멋사에서는 soup = BeautifulSoup(response.text, 'html,parser')로 가르침

# file = open("daum.html","w",encoding='UTF-8') #daum.html이란 파일을 만들고, 그걸 file이란 변수에 담을거야
# file.write(response.text) #파일에 쓸거야. response.text라는 html text를
# file.close #파일 닫아줘
# r =  read 읽기 전용만 됨
# w = write 쓰기도 가능
# a = append 기존의 파일에 새로운 내용을 덧붙임

# print(soup.title)
# print(soup.title.string)
# print(soup.span) span태그 첫번째만 찾을때.
# print(soup.findAll('span')) span태그를 모두 찾고싶을때

# html 문서에서 모든 a중 link_favorsch태그를 가져오는 코드
results = soup. findAll('a','link_favorsch')

#파일로 출력하기
search_rank_file = open('rankresult.txt','w', encoding='UTF-8')


print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))


for result in results:
    #파일 출력의 결과는 이걸로 해줘.
    search_rank_file.write(str(rank)+"위:"+result.get_text()+'\n')
    
    # print(result.get_text(), "\n") #\n 줄바꿈 #실검에서 text만 출력
    print(rank,"위:", result.get_text(),'\n')
    rank += 1




#함수란 자주 사용되는 코드를 묶어 사용할 수 있게 하는 것. 반복적인 작업을 줄이는 파이썬의 문법
#모듈이란 파이썬에서 자주 쓰이는 코드를 모아놓은 파일. 자주쓰는 클래스, 변수, 함수들을 모아놓은 파일이라고 생각하면 됨.

#get함수는 응답값을 뱉어냄 = return 응답 값. 즉 응답 값을 만들어서 돌려주는 함수

#요청하고 응답받기
#코드 내 이런 모듈을 사용할거야라고 명시하는 것이 'import'
# requests.get(url) -> 리퀘스트 안 겟 함수를 사용하고. 겟 함수는 url을 재료로 한다
# requests.get은 요청을 보내는 기능. get요청을 보내는 기능. 
# 요청을 보내는 기능에는 put, get, post, delete 등이 있음

#요청과 응답은 꼭 붙어다님
#클라이언트는 요청을 하는 존재, 서버는 응답을 하는 존재. 서버는 요청에 대한 응답을 하는 존재임. 클라이언트는 응답 받은 값으로 무언가를 함.

# requests.get(url) -> 마을조립키트.집 조립기계.(빨간블록) retrun값으로 집이 옴
# requests.get(url) -> return: requests.response

# <Response [200]> 200은 보통 성공이란 숫자를 의미함
# response는 requests.get(url)를 통해 응답받은 응답 값을 response통에 담겨오는 것. 저 통에서 원하는 정보만 가져올 수 있음.


#print(response.url)

#print(response.content)

#print(response.encoding)

#print(response.headers)

#print(response.json)

#print(response.links)

#print(response.ok)

# print(response.status_code)

# str은 문자타입이라는 것

#BeaufirulSoup = 뭉쳐져 있는 문자열을 하나씩 떼서 통에다 담아주는 함수. 함수를 사용하기 위해서는 data와 파싱 방법이 필요,
#data란 통에 담을 데이터. 이미 requests를 이용해 다음 사이트의 html을 가져왔음
#파싱이란 우리의 문서나 데이터를 의미있게 변경하는 작업. 뭉쳐져 있는 문자열을 의미있게 변경.파싱을 도와주는 프로그램을 파서