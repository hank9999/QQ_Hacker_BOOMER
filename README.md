# QQ_Hacker_BOOMER

骗子轰炸框架，请根据抓包格式修改

# 请先抓包确定GET或POST再使用对应文件夹里的文件

# 使用方法

## 安装python3
## 抓包后修改提交格式
### 1.修改url部分(如可能需要base64加密或时间戳，请在循环内部添加)
POST修改位置
```python
r = requests.post(url='http://xxx.com/up.php',
                  data={'u': user1, 'p': userpass, 'tijiao': '%E6%8F%90%CD%8F%CD%8F%CD%8F%CD%8F%E4%BA%A4'},
                  headers={'Conten  t-Type': 'application/x-www-form-urlencoded'},
                  timeout = 2)
```
GET修改位置
```python
url = "http://xxxx.com/up.php?" + "user=" + user1 + "&pass=" + userpass
```
### 2.修改线程
修改位置，默认32线程
```python
for i in range(32):  # 简易多线程
```
## 启动
### Windows 平台
在对应目录打开cmd，执行python main_GET.py / python main_POST.py启动
结束时关闭关闭窗口即可结束
### Linux 平台
在对应目录执行python3 main_GET.py / python3 main_POST.py启动
结束时Ctrl+C将其结束
