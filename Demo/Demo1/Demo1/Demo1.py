# 利用 urllib模块

import urllib.request

response = urllib.request.urlopen('https://www.baidu.com')


if __name__ == '__main__':
    # 打印百度页面HTML
    print(response.read().decode('utf-8'))


