import requests


res = requests.get('http://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.1c7f61bfCBJT13&cat=50021913&s=60&q=%CD%BC%CA%E9&style=g&active=1&type=pc#J_Filter')

print(res.text)