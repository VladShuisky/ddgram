import logging
from instascrape import Reel

logging.basicConfig(level=logging.DEBUG)

SESSIONID = 'qvf08b:1719402525554'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
    Safari/537.36 Edg/79.0.309.43",
    "cookie": f'sessionid={SESSIONID};'
}

reel_url = 'https://www.instagram.com/reel/C6nNjwwgmuk/?utm_source=ig_web_copy_link'

reel = Reel(reel_url)

reel.scrape(headers=headers)

reel.download(fp='home/vlad/razr/ddinstagram/reel1.mp4')

print('ok!')