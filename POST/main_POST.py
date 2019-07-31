import random
import string
import requests
import threading

times = 0


def start_bom():
    var = 1
    while var == 1:
        global times
        times = times + 1
        user1 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 9))
        pass1 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 6))
        pass2 = ''.join(random.sample(
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
             'c', 'v',
             'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K',
             'L', 'Z',
             'X', 'C', 'V', 'B', 'N', 'M'], 3))
        pass3 = ''.join(random.sample(['!', '@', '#', '$', '%', '^', '&', '*', ',', '.', '/'], 2))
        userpass = str(pass1 + pass2 + pass3)
        r = requests.post(url='http://xxx.com/up.php',
                          data={'u': user1, 'p': userpass, 'tijiao': '%E6%8F%90%CD%8F%CD%8F%CD%8F%CD%8F%E4%BA%A4'},
                          headers={'Conten  t-Type': 'application/x-www-form-urlencoded'},
                          timeout = 2)
        print(times)
        print("USER=" + user1)
        print("PASS=" + userpass)
        print(r.text)
        print("-------------------------------------------")


event_obj = threading.Event()
for i in range(32):  # 简易多线程
    t = threading.Thread(target=start_bom(), args=(event_obj,))
    t.setDaemon(True)
    t.start()
