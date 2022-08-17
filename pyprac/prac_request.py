import requests

r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
temp = r.json()

rows = temp['RealtimeCityAir']['row']

for row in rows:
    gu_name = row['MSRSTE_NM']
    gu_mise = row['IDEX_MVL']
    if gu_mise < 60:
        print(gu_name, gu_mise)
