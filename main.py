import csv
from requests.exceptions import RequestException
import requests
import json
from pyecharts.charts import Map
from pyecharts import options as opts

def get_page(url):
    """
        获取网页的源代码
    :param url:
    :return:
    """
    try:
        headers = {
            "authoration":"apicode","apicode":"cd0b3e5c33254e1a884180ed8e390218"

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
    return country

def main():
    """
    主函数
    :return:
    """
    url = "http://api.yonyoucloud.com/apis/dst/ncov/wholeworld"
    data_json = get_page(url) #从用友中获得原始的数据
    dic = json.loads(data_json) #转换为字典格式
    nations = DealDate(dic)#得出每个国家的数据情况

    with open(r"C:\Users\ZB\Desktop\作业二\filename.csv", "r", encoding='utf-8-sig') as csv_file:
        reader = csv.reader(csv_file)
        readDict = dict(reader)

    fin_data = [] #最终数据
    for nat in  nations:
        chname = nat['provinceName']#中文名字
        ename = readDict.get(chname)#和地图集相同的英文名字
        if ename==None:
            continue
        fin_data.append((ename,str(nat['confirmedCount'])))#添加到最终数据中

    map_p = Map(init_opts=opts.InitOpts(width='1500px',height='675px'))
    map_p.set_global_opts(title_opts=opts.TitleOpts(title="实时疫情图"), visualmap_opts=opts.VisualMapOpts(max_=300000))
    map_p.add("确诊病例数",fin_data,maptype="world")
    map_p.render("index.html")  # 生成html文件

if __name__ == '__main__':
    main()