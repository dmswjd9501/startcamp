import requests
from bs4 import BeautifulSoup
# 1. url 설정
url = 'https://finance.naver.com/marketindex/exchangeList.nhn'
# 2. 요청 보내기
response = requests.get(url).text
# 3. HTML 문서로 바꾸기
soup = BeautifulSoup(response, 'html.parser')
# 4. 원하는 내용 선택자로 뽑아내기
table = soup.select('body > div > table > tbody > tr')
# body > div > table > tbody > tr:nth-child(1) > td.sale
for tr in table:
    print(tr.select('td.sale')[0].text)
    # 리스트가 1개인게 확실하다면 tr.select_one('td.sale') 혹은 tr.select[0] 라고 해주면 ok