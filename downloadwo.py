import requests
import json
import re
import os

def get_filename_from_cd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]


def download(url):
    r = requests.get(url, allow_redirects=True)
    filename = get_filename_from_cd(r.headers.get('content-disposition'))
    if os.path.exists(filename):
        return
    open(filename, 'wb').write(r.content)
                           
headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'origin': 'https://m.alltuu.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://m.alltuu.com/',
    'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
}


urls=["https://v4c.alltuu.com/a3cd6ba9aa5798635f5aae5012f585c0/66f41afc/rest/v4c/fpl/a1565760104/n60/o4/p2/pw/s1602761033/t1727241889021/v1",
      "https://v4c.alltuu.com/160c18e949763f892a789143c08f2acd/66f41afc/rest/v4c/fpl/a1565760104/n60/o4/p3/pw/s1602761033/t1727241889021/v1",
      "https://v4c.alltuu.com/39e1f69cbf327c82f172c08bab602601/66f41afc/rest/v4c/fpl/a1565760104/n60/o4/p4/pw/s1602761033/t1727241889021/v1",
      "https://v4c.alltuu.com/db620ae017c3fd73958931ba80cca3ef/66f41b16/rest/v4c/fpl/a1565760104/n60/o4/p5/pw/s1602761033/t1727241889021/v1",
      "https://v4c.alltuu.com/3f3dc45bfae7e286ae00a57c1b2482b9/66f41b27/rest/v4c/fpl/a1565760104/n60/o4/p6/pw/s1602761033/t1727241889021/v1",
      "https://v4c.alltuu.com/669fb2853bbd05db1e2276ce4c877caa/66f41b27/rest/v4c/fpl/a1565760104/n60/o4/p7/pw/s1602761033/t1727241889021/v1",
      "https://v4c.alltuu.com/f0303cdd7a3ccd6c87bf6f1db853d3d7/66f41b28/rest/v4c/fpl/a1565760104/n60/o4/p8/pw/s1602761033/t1727241889021/v1"]

for url in urls:
    response = requests.get(
        url,
        headers=headers,
    )
    list=json.loads(response.content.decode())
    for photo in list.get("d"):
        download(photo.get("ol"))