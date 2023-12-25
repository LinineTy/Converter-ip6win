# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 19:23:57 2023

@author: 19738
"""

import socket
import tkinter as tk
import time
from tkinter import ttk

def get_ip_address(domain_1):
    try:
        ip_address = socket.gethostbyname(domain_1)
        return ip_address
    except (socket.gaierror, IndexError) as e:
        print(f"Error: {e}")
        return None

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

def show_result():
    domain = entry.get()
    domain_1 = entry.get()
    ipv6_address = get_ipv6_address(domain)
    ip_address = get_ip_address(domain_1)

    if ipv6_address and ip_address:
        modified_ipv6 = replace_colon_with_dash(ipv6_address)
        result_label.config(text=f"您查询的域名是 ‘ {domain} ’ \n\n查询到的的IPv4地址为: {ip_address}\n\nIPv6地址为：{ipv6_address}\n\n转换格式后的IPv6地址为: {modified_ipv6}")
        #创建后删除复制按钮
        copy_button = tk.Button(window, text="复制转换后的地址", command=copy_result)
        copy_button.pack(pady=5)
    else:
        if ip_address:
            result_label.config(text=f"您查询的域名是 ‘ {domain} ’ \n\n查询到的的IPv4地址为: {ip_address}\n\n未找到IPv6地址")
            
        elif ipv6_address:
            modified_ipv6 = replace_colon_with_dash(ipv6_address)
            result_label.config(text=f"您查询的域名是 ‘ {domain} ’ \n\n查询到的的IPv6地址为: {ipv6_address}\n\n转换格式后的IPv6地址为: {modified_ipv6}")
            #创建后删除复制按钮
            copy_button = tk.Button(window, text="复制转换后的地址", command=copy_result)
            copy_button.pack(pady=5)
            time.sleep = 1
            copy_button.destroy()
        else:
            result_label.config(text="无法获取IP地址")

def copy_result(): 
    domain = entry.get()
    ipv6_address = get_ipv6_address(domain)
    if ipv6_address:
        modified_ipv6 = replace_colon_with_dash(ipv6_address)
        result_label.config(text=f"{modified_ipv6}")
        window.clipboard_clear() 
        window.clipboard_append(result_label.cget("text"))
        window.update()
        result_label.config(text=f"转换格式后的IPv6地址是：\n\n{modified_ipv6}\n\n已为您复制到系统剪贴板~")

# 创建主窗口
window = tk.Tk()
window.title("IPv6 地址查询工具")

# 设置窗口大小
window.geometry("700x500")

# 设置窗口背景颜色
window.configure(bg="#FFDAB9")

# 创建样式
style = ttk.Style()
style.configure("TButton",
                background="#808080",  # 灰色背景
                foreground="black",   # 黑色文字
                padding=(10, 5),       # 按钮内边距
                font=('Helvetica', 12),  # 字体和大小
                borderwidth=2,          # 边框宽度
                relief="flat",          # 去除按钮凸起效果
                )

# 创建标签和输入框
label = tk.Label(window, text="请输入你想要查询的域名:", bg="#FFDAB9", font=('Helvetica', 14))
label.pack(pady=30)

entry = tk.Entry(window, font=('Helvetica', 14))
entry.pack(pady=0)

# 创建按钮
button = ttk.Button(window, text="查询", command=show_result, style="TButton")
button.pack(pady=30)

# 创建结果标签
result_label = tk.Label(window, text="", bg="#FFDAB9", font=('Helvetica', 14))
result_label.pack(pady=10)

# 启动主循环
window.mainloop()
