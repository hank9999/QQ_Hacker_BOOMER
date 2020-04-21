# QQ_Hacker_BOOMER

骗子轰炸框架，请根据抓包格式修改

请先抓包确定GET或POST再使用对应文件

更优雅的异步并发方案

# 使用方法

## 一、安装python3
## 二、抓包后修改提交格式
### 1.修改url部分(如可能需要base64加密或时间戳，请在循环内部添加)
POST修改位置
```python
data = {'user': user1, 'pass': password}

main('', 16)
```
GET修改位置
```python
params = {'user': user1, 'pass': password}

main('', 16)
```

## 三、启动
### Windows 平台
##### 在对应目录打开cmd，执行python main_GET.py / python main_POST.py启动
##### 结束时 Ctrl+C 或 关闭窗口 均可结束
### Linux 平台
##### 在对应目录执行python3 main_GET.py / python3 main_POST.py启动
##### 结束时 Ctrl+C 将其结束
