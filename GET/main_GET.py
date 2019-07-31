import random
import string
import urllib.request
import threading

times = 0


def start_bom():
    var = 1
    while var == 1:
        try:
            global times
            times = times + 1
            user1 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 9))
            pass1 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 6))
            pass2 = ''.join(random.sample(
                ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z',
                 'x',
                 'c', 'v',
                 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J',
                 'K',
                 'L', 'Z',
                 'X', 'C', 'V', 'B', 'N', 'M'], 3))
            pass3 = ''.join(random.sample(['!', '@', '#', '$', '%', '^', '&', '*', ',', '.', '/'], 2))
            userpass = str(pass1 + pass2 + pass3)
            url = "http://xxxx.com/up.php?" + "user=" + user1 + "&pass=" + userpass
            request1 = urllib.request.urlopen(url, timeout=2)
            print(times)
            print("USER=" + user1)
            print("PASS=" + userpass)
            print(str(request1.read(), 'utf8'))
            print("-------------------------------------------")
        except:
            print("Error!(Maybe timeout)")


if __name__ == "__main__":
    event_obj = threading.Event()
    for i in range(256):  # 简易多线程
        try:
            t = threading.Thread(target=start_bom(), args=(event_obj,))
            t.setDaemon(True)
            t.start()
        except:
            print("Thread Create Error!")
