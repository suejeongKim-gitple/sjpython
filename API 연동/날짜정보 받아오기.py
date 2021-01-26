# https://wikidocs.net/13#f
# API는 클라이언트와 서버가 데이터를 원활하게 주고받기 위해 있는것. API는 클라이언트와 서버의 중간에서 서로간의 데이터가 잘 교환될 수 있도록 어떠한 약속을 해주는 역할을 함.

import requests #리퀘스트 모듈은 API에 요청을 보내는 모듈
import json #json은 Java script object notation의 줄임말. 주로 데이터를 주고 받을때 사용하는 포맷

city = "Seoul"
apikey = "09d6fedca11b068ba995e0331d2dd3f0"
lang = "kr"
metric = "metric"
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units={metric}" 
#or  api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric" 

result = requests.get(api)
data = json.loads(result.text) #원하는 결과값을 json타입으로 변경

# print(type(data)) #해당 값의 타입을 알고싶을때

print(data["name"],"의 날씨입니다.")
print("날씨는",data["weather"][0]["description"],"입니다.")
print("현재 온도는",data["main"]["temp"],"입니다.")
print("하지만 체감 온도는", data["main"]["feels_like"],"입니다.")
print("최저 기온은",data["main"]["temp_min"],"입니다.")
print("최고 기온은",data["main"]["temp_max"],"입니다.")
print("습도는",data["main"]["humidity"],"입니다.")
print("기압은",data["main"]["pressure"],"입니다.")
print("풍향은",data["wind"]["deg"],"입니다.")
print("풍속은",data["wind"]["speed"],"입니다.")