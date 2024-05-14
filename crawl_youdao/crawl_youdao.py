import requests 
from bs4 import BeautifulSoup
import sys
#函数部分
def youdao(word):
    base_url = f'https://www.youdao.com/result?word={word}&lang=en'#获取网页URL
    response = requests.get(base_url) # 发起HTTP请求并获取网页内容
    #检查请求是否成功
    if response.status_code ==200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # 通过BeautifulSoup提取特定的内容，这里以词汇为例
        word = soup.find('div',class_='title').get_text()
        print(f'词汇: {word}')
        #获取词汇的意思
        meaning = soup.find('ul', class_='basic')
        if meaning:
            print('简明:')
            print(meaning.get_text().strip())
        else:
            print('未找到词汇')
        return meaning
    else:
        print('未能找到页面')
#主程序
def main():
    print('请输入要搜索的单词:')
    word_to_search = input()
    youdao(word_to_search)
while(True):
    main()

















    
