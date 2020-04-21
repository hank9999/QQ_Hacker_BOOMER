import random
import string
import asyncio, aiohttp
import threading
import signal
import sys

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

async def request(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data, headers=headers) as resp:
            return [resp.status, await resp.text()]

async def once(url):
    user1 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 9))
    pass1 = ''.join(random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 6))
    pass2 = ''.join(random.sample(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z','x','c', 'v','b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J','K','L', 'Z','X', 'C', 'V', 'B', 'N', 'M'], 3))
    pass3 = ''.join(random.sample(['!', '@', '#', '$', '%', '^', '&', '*', ',', '.', '/'], 2))
    password = str(pass1) + str(pass2) + str(pass3)
    data = {'user': user1, 'pass': password}
    status, text = await request(url, data)
    print(user1 + ':' + password + ' ' + str(status))

def main(url, n):
    loop = asyncio.get_event_loop()
    times = 0
    while 1:
        print('=' * 10)
        try:
            tasks = [once(url) for i in range(n)]
            loop.run_until_complete(asyncio.wait(tasks))
            times += n
            print('times: ' + str(times))
        except KeyboardInterrupt:
            sys.exit()
        except Exception:
            sys.exit()
    loop.close()

if __name__ == "__main__":
    main('', 16)