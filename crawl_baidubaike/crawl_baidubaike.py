import requests 
from bs4 import BeautifulSoup
import sys

#函数部分
def baidu_baike(topic):
    base_url = f'https://baike.baidu.com/item/{topic}'#获取网页URL
    response = requests.get(base_url) # 发起HTTP请求并获取网页内容
    
    # 检查请求是否成功
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 通过BeautifulSoup提取特定的内容，这里以标题为例
        title = soup.find('h1').get_text()
        print(f'主题: {title}')
        
        #获取百度百科页面的简介部分
        summary = soup.find('div', class_='lemmaSummary_cFhDf J-summary')
        #获取百度百科页面的基本信息部分
        basic_info = soup.find('div', class_='basicInfo_spa7J J-basic-info')
        if summary:
            print('简介:')
            print(summary.get_text().strip())
        else:
            print('不好意思，简介未找到。')
        if basic_info:
            print('基本信息：')
            print(basic_info.get_text().strip())
        else:
            print('不好意思，基本信息未找到。')
        return title, summary, basic_info
    else:
       print('未能找到页面')
#主程序
def main():       
    print("请输入要搜索的主题：")# 要搜索的主题
    topic_to_search =input() # 输入搜索的主题
    baidu_baike(topic_to_search) # 调用函数爬取百度百科内容
    #将爬取内容写入result.txt文件中
    with open(r'result.txt', 'w', encoding='utf-8') as file:
        sys.stdout = file  # 重定向输出
        baidu_baike(topic_to_search)
    sys.stdout = sys.__stdout__#标准输出恢复为默认的控制台
    print("\n\n")
    print("注意：内容已写入 'result.txt' 文件。")
while(True):
    main()
