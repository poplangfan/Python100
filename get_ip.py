# -*- coding: utf-8 -*-
import requests
from lxml import etree
from fake_useragent import UserAgent


def get_ip():
    base_url = 'https://www.kuaidaili.com/free/inha/{}/'  # 快代理免费ip，根据自己需要抓取
    headers = {'User-Agent': UserAgent().chrome}
    for i in range(11, 16):  # 自定义抓取页数
        resp = requests.get(base_url.format(i), headers=headers)
        e = etree.HTML(resp.text)
        ips = e.xpath('//td[@data-title="IP"]/text()')  # ips,ports,types根据网站的不同而不同
        ports = e.xpath('//td[@data-title="PORT"]/text()')
        types = e.xpath('//td[@data-title="类型"]/text()')
        for ip, port, typa in zip(ips, ports, types):
            if typa == 'HTTP':
                http_ip = typa + '://' + ip + ':' + port
                text_http(http_ip, ip)
            else:
                https_ip = typa + '://' + ip + ':' + port
                text_https(https_ip, ip)


def text_ip(base_url, ip_, ip):  # 测试ip是否可用
    headers = {'User-Agent': UserAgent().chrome}
    proxies = {
        'http': ip_,
    }
    try:
        resp = requests.get(base_url, headers=headers, proxies=proxies, timeout=5)
        obj = resp.json()
        if ip == obj['origin']:
            print(ip_)
            with open('ip.txt', 'a', encoding='utf-8') as f:
                f.write(ip_ + '\n')
        else:
            print('{}不可用'.format(ip))
    except:
        print('{}超时'.format(ip))


def text_http(ip_, ip):
    base_url = 'http://httpbin.org/get'
    text_ip(base_url, ip_, ip)


def text_https(ip_, ip):
    base_url = 'https://httpbin.org/get'
    text_ip(base_url, ip_, ip)


if __name__ == '__main__':
    get_ip()
