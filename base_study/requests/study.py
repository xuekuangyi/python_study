import json

import requests

domains = 'https://yx.ciecinfo.com/'
url_to_api_1 = '/centre/getActivityAward'
edition_of_http = 'HTTP/1.1'

whole_url = domains + url_to_api_1

par = {'activNo': '21091100003', 'businessType': '4'}

res = requests.post(url=whole_url, data=par)  # post方法

json_contents = res.text
data2 = json.dumps({"Status": "false", "Msg": "该活动不是用户领券活动", "StatusCode": 500}, sort_keys=True, indent=4,
                   separators=('"', ': '))
print(data2)
print(json_contents)
print(res.status_code)  # 获取返回状态
print(res.url)
print(res.content)
