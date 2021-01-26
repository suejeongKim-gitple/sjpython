import requests
from bs4 import BeautifulSoup

BASE_URL = "https://gall.dcinside.com/board/lists"
params = {'id': 'government',}
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
resp = requests.get(BASE_URL, params=params, headers=headers)

soup = BeautifulSoup(resp.content, 'html.parser')

contents = soup.find('tbody').find_all('tr')

for i in contents:
    print('-'*15)

    # 제목ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    title_tag = i.find('a')
    # title = title_tag.text
    print("제목: ", title_tag.text)

    # 글쓴이ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    wirter_tag = i.find('td', class_='gall_writer ub-writer').find('span', class_='nickname')
    if wirter_tag is not None:
        writer = wirter_tag.text
        print("글쓴이: ", writer)
    else:
        print("글쓴이:", "없음")

    # IPㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
        # 유동이나 고닉이 아닌 글쓴이 옆에 있는 ip 추출
    # ip_tag = i.find('td', class_='gall_writer ub-writer').find('span', class_='ip')
    # if ip_tag is not None:  # None 값이 있으므로 조건문을 통해 회피 
    #     ip = ip_tag.text
    #     print("ip: ", ip)

    #날짜ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    data_tag = i.find('td', class_='gall_date')
    date_dict = data_tag.attrs
    
    if len(date_dict) is 2:
        print("날짜:", date_dict['title'])
    else:
        print("날짜:", data_tag.text)
        pass
  
    #조회수ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    view_tag = i.find('td', class_='gall_count')
    print("조회수:", view_tag.text)

    #추천수ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    recommend_tag = i.find('td',class_='gall_recommend')
    print("추천수:", recommend_tag.text)

    #링크ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
    link_tag = i.find('a')['href']
    A = BASE_URL + link_tag
    B = A.replace("https://gall.dcinside.com/board/lists/board/view/", "https://gall.dcinside.com/board/view/")

    # right = BASE_URL + link_tag.remove('/lists/board/')
    print("링크: ", B)

    #글 내용
    



# https://gall.dcinside.com/board/lists?id=government&no=13166493&_rk=tDL&page=1
# https://gall.dcinside.com/board/view/?id=government&no=13166493&_rk=tDL&page=1



# url = "https://gall.dcinside.com/board/lists?id=government"

# filename = "govermentgall.csv"
# f = open(filename, "w", encoding="utf-8-sig", newline="") #엑셀파일을 열때 한글이 깨지면 utf-8-sig
# writer = csv.writer(f)

# title = "번호	제목	글쓴이	작성일	조회	추천".split("\t")
# print(type(title))
# writer.writerow(title)

# for page in range(1, 10):
#     res = requests.get(url + str(page))
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, "lxml")

#      data_rows = soup.find("table", attrs={"class":"gall_list"}).find("td").find_all("a")
    