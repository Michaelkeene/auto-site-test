import asyncio
import aiohttp
from ssl import SSLCertVerificationError

async def url_grabber(url):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
                             "/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36"}
    async with aiohttp.ClientSession(headers=headers) as session:
        try:
            async with session.get(url) as r:
                content = await r.text()
                print(url, "fine")
        except SSLCertVerificationError:
            print(url, "ssl error")
        except Exception:
            print("BROKEN URL, "*3, url, "IS BROKEN")


sites = [x.strip() for x in open("URL ssl auto test/URLS to Test.txt", "r")]


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([url_grabber(x) for x in sites]))




