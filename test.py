import requests
from bs4 import BeautifulSoup as bs
import re

def extract_numbers_after_text(text):
    numbers_after_text = re.findall(r"javascript:\$.readBoard\('(\d+)'\)", text)
    
    if numbers_after_text:
        numbers = numbers_after_text[0]
        return numbers
    else:
        return None
    
def get_link(href):
    seq = extract_numbers_after_text(href)
    return "http://www.futsal.or.kr/brd_boardRead.action?seq={}&board_id=03".format(seq)
    
page = requests.get("http://www.futsal.or.kr/brd_boardLoad.action?board_id=03")
soup = bs(page.text, "html.parser")
elements = soup.select('table.table_type1.wp100 td a')

specific_strings = ['여자', '여성']
filtered_array = [string for string in elements if any(specific in string.text for specific in specific_strings)]

for index, element in enumerate(filtered_array, 1):
		print("{} 번째 게시글의 제목: {}".format(index, element.text))
		print("{} 번째 게시글의 주소: {}".format(index, get_link(element.attrs['href'])))
		

