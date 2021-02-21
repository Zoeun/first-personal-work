import requests
from requests.exceptions import RequestException
import json
from lxml import etree
import csv
import re
import time
from urllib import parse
import time
import requests
import json
import re
import pprint
from pyecharts.charts import Map, Geo
from pyecharts import options as opts


def get_page(url):
    """
        获取网页的源代码
    :param url:
    :return:
    """
    try:
        headers = {
            "authoration": "apicode", "apicode": "cd0b3e5c33254e1a884180ed8e390218",
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def DealDate(data):

    data=data["data"]["continent"]
    Asia=data[0]["country"]
    Europe=data[1]["country"]
    NorthAmerica=data[2]["country"]
    SouthAmerica=data[3]["country"]
    Africa=data[4]["country"]
    Oceania=data[5]["country"]
    country=Asia+Europe+NorthAmerica+SouthAmerica+Africa+Oceania

url = 'https://api.yonyoucloud.com/apis/dst/ncov/wholeworld'

text = get_page(url)

dic = json.loads(text)

data = dic

data=data["data"]["continent"]
Asia=data[0]["country"]
Europe=data[1]["country"]
NorthAmerica=data[2]["country"]
SouthAmerica=data[3]["country"]
Africa=data[4]["country"]
Oceania=data[5]["country"]
country=Asia+Europe+NorthAmerica+SouthAmerica+Africa+Oceania

print(Asia)

map_p = Map()
map_p.set_global_opts(title_opts=opts.TitleOpts(title="实时疫情图"), visualmap_opts=opts.VisualMapOpts(max_=100))
map_p.add("确诊", data, maptype="Asia")
map_p.render("ncov.html")  # 生成html文件