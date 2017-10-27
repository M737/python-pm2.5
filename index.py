

import requests
from bs4 import BeautifulSoup as BS
from pyecharts import Geo

def get_data(url):

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3192.0 Safari/537.36',
        'Referer':'http://www.cnkongqi.com/pc/100000.htm',
        'Host':'www.cnkongqi.com'}
    res = requests.get(url,headers=headers)
    res.encoding = 'utf-8'
    soup = BS(res.text, 'lxml')
    nodes_soup = soup.findAll('tr')
    items = []
    num = []
    for node in nodes_soup:
        if node.select('td a'):
            if node.select('td')[2].get_text() != '-':
                city = node.select('td a')[0].get_text()
                data = node.select('td')[2].get_text()
                num.append(int(data))
                a = (city,int(data))
                items.append(a)
    return items,max(num)
def echarts(data,max_num):
    geo = Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center",
    width=1200, height=600, background_color='#404a59')
    attr, value = geo.cast(data)
    geo.add("", attr, value, visual_range=[0, max_num], visual_text_color="#fff",
            symbol_size=15, is_visualmap=True)
    geo.render('air_map.html')


def main():
    url = 'http://www.cnkongqi.com/pc/order.htm'
    data, max_num = get_data(url)
    echarts(data, max_num)
    
if __name__ == '__main__':
    main()
    
