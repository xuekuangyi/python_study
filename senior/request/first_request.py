import json

import requests

payload = {'page': '1', 'per_page': '10'}
r = requests.get("https://yx.ciecinfo.com/centre/getCouponShop", params={'userPhone': '13810083560',
                                                                         'rows': '1', 'businessType': '1',
                                                                         'couponStat': '0'})
d = requests.get('https://apitest.91jieshu.com/together/cash/get-cash-list?uid=1&pageSize=20&page=0')
rr = r.text
print(rr)
json_dicts = json.dumps(rr, indent=4)
print(json_dicts)


# print(r.content)
# print(r.url)
# print(r)
# print(d)
