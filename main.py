import urllib

import null as null
import requests
from lxml import etree
import math
import datetime
import xlwt
import re
from requests.adapters import HTTPAdapter

total_num = 1000

total_num = math.ceil(total_num)
res = []

num = 1
print(total_num)
count = 0

for page_index in range(1, total_num + 1):

    url = "https://www.sanven.cn/sanwen/shenghuosanwen/list_17_" + str(page_index) + ".html"
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=8))
    s.mount('https://', HTTPAdapter(max_retries=8))
    # print(url)
    rop = requests.get(url)
    rop.encoding = "utf-8"
    html_text = rop.text
    # txts = re.findall(r'<a title=(.*?) target="_blank', html_text)
    urls = re.findall(r' <a href=\"(.*?)\" target=\"_blank\">', html_text)
    # for txt in urls:
    #    print(txt)

    for url_sec in urls:
        if "sanwen" in url_sec:
            title = "散文" + str(count)
            data = open(title + ".txt",
                        'a',
                        encoding="utf-8")
            count += 1
            url_comb = 'https://www.sanven.cn/' + url_sec
            print(url_comb)
            rop_second = requests.get("https://www.sanven.cn"+url_sec)
            rop_second.encoding = "GB2312"
            html_sec_text = rop_second.text
            # print(html_sec_text)
            content = re.findall(r'<p>([\s\S]*?)</p>', html_sec_text)
            for txt in content:
                try:

                    if "相关" in txt:
                        break
                    data.write(txt.replace(r'\&(.*?)quo', "").replace("&nbsp", ""))
                except IndexError:
                    print("Index Error")
            data.close()

            # txts_sec = re.findall(r'<a title=(.*?) target="_blank')

