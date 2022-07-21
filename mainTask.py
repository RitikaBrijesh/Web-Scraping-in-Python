from sqlite3 import connect
import requests
from bs4 import BeautifulSoup
import json
import csv
import time
import MySQLdb

start=time.time()

list=[]

print('<<<<<<<<<<<<<<<<<<<<<<<<<< First URL >>>>>>>>>>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1015"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()


    #print(type(title))
    #print(type(price))

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result1={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result1)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<Second URL >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1015"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()


    #print(type(title))
    #print(type(price))

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result2={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result2)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Third URL >>>>>>>>>>>>>>>>>>>>>>>>>>>')

try:
    #url="https://www.amazon.{}/dp/{}".format(country,Asin)
    url="https://www.amazon.de/dp/000004458X"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()


    #print(type(title))
    #print(type(price))

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    # result="[{'title':{{}}, 'image_url':image_src, 'price':price, 'detail':detail}]".format(title)
    result3={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result3)

except Exception as e:
    print(e)


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Fourth URL >>>>>>>>>>>>>>>>>>>')

try:
    url="https://www.amazon.fr/dp/000004458X"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()


    #print(type(title))
    #print(type(price))

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result4={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result4)

        

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<< Fifth URL >>>>>>>>>>>>>>>>>>>>>>>')
try:
    
    url="https://www.amazon.de/dp/1002198"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()


    #print(type(title))
    #print(type(price))

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result5={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result5)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<< 6th URL >>>>>>>>>>>>>>>>>')

try:
    url="https://www.amazon.fr/dp/1002198"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()


    #print(type(title))
    #print(type(price))

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result6={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result6)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 7th URL >>>>>>>>>>>>>>>>>>>>>>>>>')

try:
    url="https://www.amazon.fr/dp/1002791"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()


    #print(type(title))
    #print(type(price))

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')


    result7={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result7)
except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< 8th URL >>>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.it/dp/1002791"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result8={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result8)
except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<< 9th URL >>>>>>>>>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1002864"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result9={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result9)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<< 10th URL >>>>>>>>>>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1002864"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result10={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result10)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<< 11th url >>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1003704"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()


    #print(type(title))
    #print(type(price))

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result11={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result11)


except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<< 12th url >>>>>>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1003704"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result12={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result12)

except Exception as e:
    print(url, 'not available')


print('>>>>>>>>>>>>>>>>>>>>>>>>>> 13th url >>>>>>>>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1003763"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result13={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result13)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<< 14th URL >>>>>>>>>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1003763"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()


    #print(type(title))
    #print(type(price))

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result14={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result14)

except Exception as e:
    print(url, 'not available')
    



print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 15th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1004271"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result15={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result15)

except Exception as e:
    print(url, 'not available')

#######################################################################################################
#######################################################################################################
#######################################################################################################


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 16th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.it/dp/1004271"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result16={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result16)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 17th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/000101742X"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-size-base a-color-price a-color-price').get_text()

    #Product Image Url
    image_src=soup2.find(id='imgBlkFront')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-expander-content a-expander-partial-collapse-content').get_text()


    #print(type(title))
    #print(type(price))

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result17={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result17)

except Exception as e:
    print(url, 'not available')



print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 18th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/000101742X"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-color-base').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='normal').get_text()


    #print(type(title))
    #print(type(price))

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result18={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result18)



except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 19th url >>>>>>>>>>>>>>>>>')
try:
    # URL="https://www.amazon.",i[3],"/dp/",i[2]
    # url=''.join(URL)
    # print(type(url))
    # print(url, 'not available')
    #url="https://www.amazon.{}/dp/{}".format(country,Asin)
    url="https://www.amazon.de/dp/1017519"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()


    #print(type(title))
    #print(type(price))

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result19={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result19)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 20th url >>>>>>>>>>>>>>>>>')
try:
    # URL="https://www.amazon.",i[3],"/dp/",i[2]
    # url=''.join(URL)
    # print(type(url))
    # print(url, 'not available')
    #url="https://www.amazon.{}/dp/{}".format(country,Asin)
    url="https://www.amazon.fr/dp/1017519"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()


    #print(type(title))
    #print(type(price))

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')


    result20={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result2)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 21th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/000102163X"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-size-base a-color-price a-color-price').get_text()

    #Product Image Url
    image_src=soup2.find(id='imgBlkFront')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-expander-content a-expander-partial-collapse-content').get_text()


    #print(type(title))
    #print(type(price))

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result21={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result21)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 22th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/000102163X"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-color-base').get_text()

    #Product Image Url
    image_src=soup2.find(id='imgBlkFront')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='normal').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result22={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result22)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 23th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1022369"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result23={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result23)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 24th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.it/dp/1022369"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result24={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result24)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 25th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1022857"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result25={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result25)
except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 26th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.it/dp/1022857"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result26={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result26)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 27th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1032666"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result27={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result27)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 28th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1032666"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result28={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result28)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 29th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1034677"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result29={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result29)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 30th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1034677"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result30={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result30)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 31th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1034936"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result31={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result31)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 32th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1034936"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result32={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result32)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 33th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1034944"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result33={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result33)


except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 34th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1034944"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result34={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result34)
except Exception as e:
    print(url, 'not available')


####################################################################################################################
####################################################################################################################
####################################################################################################################


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 35th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1035002"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()


    #print(type(title))
    #print(type(price))

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result35={
            'title':title, 
            'image_url':src, 
            'price':price, 
            'detail':detail
        }

    list.append(result35)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 36th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1035002"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')


    result36={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result36)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 37th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1035029"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result37={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result37)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 38th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1035029"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')


    result38={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result38)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 39th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1035053"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result39={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result39)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 40th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.es/dp/1035053"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result40={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result40)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 41th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1035053"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result41={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result41)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 42th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1035339"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result42={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result42)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 43th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1035339"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result43={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result43)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 44th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1036866"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result44={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result44)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 45th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.es/dp/1036866"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()


    #print(type(title))
    #print(type(price))

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result45={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result45)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 46th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1036866"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result46={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result46)
except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 47th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1037137"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result47={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result47)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 48th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1037137"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()


    #print(type(title))
    #print(type(price))

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result8={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result48)
except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 49th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1037188"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()


    #print(type(title))
    #print(type(price))

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result49={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result49)

except Exception as e:
    print(url, 'not available')


##################################################################################################################
##################################################################################################################
##################################################################################################################

print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 50th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1037188"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result50={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result50)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 51th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1037994"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result51={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result51)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 52th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1037994"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')


    result52={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result52)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 53th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/000103863X"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-size-base a-color-price a-color-price').get_text()

    #Product Image Url
    image_src=soup2.find(id='imgBlkFront')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-expander-content a-expander-partial-collapse-content').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result53={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result53)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 54th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/000103863X"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='imgBlkFront')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='normal').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result54={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result54)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 55th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1039466"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result55={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result55)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 56th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1039466"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result56={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result56)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 57th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1040871"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result57={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result57)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 58th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.it/dp/1040871"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result58={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result58)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 59th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1040979"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')


    result59={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result59)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 60th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1040979"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result60={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result60)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 61th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1040987"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')


    result61={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result61)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 62th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1040987"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result62={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result62)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 63th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1041002"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result63={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result63)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 64th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/11040987"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result64={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result64)
except Exception as e:
    print(url, 'not available')


#####################################################################################################################
####################################################################################################################
####################################################################################################################

print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 65th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1041991"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result65={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result65)

except Exception as e:
    print(url, 'not available')



print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 66th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1041991"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result66={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result66)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 67th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/000104317X"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-size-base a-color-price a-color-price').get_text()

    #Product Image Url
    image_src=soup2.find(id='imgBlkFront')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-expander-content a-expander-partial-collapse-content').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result67={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result67)

except Exception as e:
    print(url, 'not available')



print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 68th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/000104317X"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-size-base a-color-price a-color-price').get_text()

    #Product Image Url
    image_src=soup2.find(id='imgBlkFront')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='normal').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result68={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result68)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 69th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1043331"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result69={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result69)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 70th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1043331"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')


    result70={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result70)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 71th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/000104348X"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-color-price a-text-bold').get_text()

    #Product Image Url
    image_src=soup2.find(id='imgBlkFront')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-expander-content a-expander-partial-collapse-content').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result71={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result71)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 72th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/000104348X"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-color-price a-text-bold').get_text()

    #Product Image Url
    image_src=soup2.find(id='imgBlkFront')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-row').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result72={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result72)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 73th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1043498"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result73={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result73)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 74th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1043498"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result74={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result74)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 75th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1043773"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result75={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result75)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 76th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1043773"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result76={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result76)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 77th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/000104396X"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-color-base').get_text()

    #Product Image Url
    image_src=soup2.find(id='imgBlkFront')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-expander-content a-expander-partial-collapse-content').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result77={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result77)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 78th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/000104396X"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-color-base').get_text()

    #Product Image Url
    image_src=soup2.find(id='imgBlkFront')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='normal').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result78={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result78)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 79th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1048325"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result79={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result79)

except Exception as e:
    print(url, 'not available')


####################################################################################################################
####################################################################################################################
####################################################################################################################


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 80th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1048325"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result80={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result80)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 81th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1049119"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result81={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result81)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 82th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1049119"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result82={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result82)

except Exception as e:
    print(url, 'not available')



print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 83th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1057774"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()
    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result83={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result83)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 84th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1057774"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()
    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result84={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result84)

except Exception as e:
    print(url, 'not available')



print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 85th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1057790"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result85={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result85)

except Exception as e:
    print(url, 'not available')




print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 86th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.es/dp/1057790"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()
    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result86={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result86)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 87th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1057790"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result87={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result87)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 88th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1057812"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result88={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result88)

except Exception as e:
    print(url, 'not available')



print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 89th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.es/dp/1057812"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result89={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result89)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 90th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1057812"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result90={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result90)

except Exception as e:
    print(url, 'not available')

print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 91th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1057987"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result91={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result91)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 92th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1057987"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result92={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result92)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 93th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1059238"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()
    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result93={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result93)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 94th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1059238"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result94={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result94)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 95th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1060619"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()
    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result95={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result95)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 96th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1060619"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result96={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result96)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 97th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1060694"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result97={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result97)
except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 98th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.es/dp/1060694"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()
    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result98={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result98)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 99th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.fr/dp/1060694"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()
    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')

    result99={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result99)

except Exception as e:
    print(url, 'not available')


print('<<<<<<<<<<<<<<<<<<<<<<<<<<<< 100th url >>>>>>>>>>>>>>>>>')
try:
    url="https://www.amazon.de/dp/1061305"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #product title
    title = soup2.find(id='productTitle').get_text()

    #Product Price
    price = soup2.find(class_='a-offscreen').get_text()

    #Product Image Url
    image_src=soup2.find(id='landingImage')
    src=image_src.get('src')

    #Product Detail
    detail=soup2.find(class_='a-list-item').get_text()

    print(f'Product Title : {title}')
    print(f'Product Image URL : {src}')
    print(f'Product Price : {price}')
    print(f'Product Detail : {detail}')


    result100={
        'title':title, 
        'image_url':src, 
        'price':price, 
        'detail':detail
    }

    list.append(result100)

except Exception as e:
    print(url, 'not available')


# with open('output.json', 'w') as file:
#         json.dump(list,file)

# file.close()

print(list)

mydb=MySQLdb.connect(host="localhost", user="root", password="MySQL@123",database="new_schema")
mycursor=mydb.cursor()

mycursor.executemany("""
    INSERT INTO products (title, image_url, price, detail)
    VALUES (%(title)s, %(image_url)s, %(price)s, %(detail)s)""",list)

mydb.commit()

end=time.time()
run_time=end-start

print('Execution time : ',run_time,'seconds')


