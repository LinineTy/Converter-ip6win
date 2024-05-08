# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:49:14 2023

@author: 19738
"""

import socket

def get_ipv6_address(domain):
    try:
        # 获取IPv6地址
        ipv6_address = socket.getaddrinfo(domain, None, socket.AF_INET6)[0][4][0]
        return ipv6_address
    except (socket.gaierror, IndexError) as e:
        print(f"Error: {e}")
        return None

def replace_colon_with_dash(ipv6_address):
    return ipv6_address.replace(':', '-')

if __name__ == '__main__':
    # 获取用户输入的域名
    domain = input("请输入你想要查询的域名：")

    ipv6_address = get_ipv6_address(domain)

    if ipv6_address:
        modified_ipv6 = replace_colon_with_dash(ipv6_address)
        print(f"域名 {domain} 的IPv6地址为: {ipv6_address}")
        print(f"替换冒号为破折号后的IPv6地址为: {modified_ipv6}")
    else:
        print("无法获取IPv6地址")
