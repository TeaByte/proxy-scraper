import aiohttp, asyncio
from re import compile

TIMEOUT: int = 15
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
REGEX = compile(
    r"(?:^|\D)?(("+ r"(?:[1-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"\." + r"(?:\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])"
    + r"):" + (r"(?:\d|[1-9]\d{1,3}|[1-5]\d{4}|6[0-4]\d{3}"
    + r"|65[0-4]\d{2}|655[0-2]\d|6553[0-5])")
    + r")(?:\D|$)"
)

scrapped_proxies = []
with open('proxies.txt', 'w') as proxies: proxies.write('')
proxies = open('proxies.txt', 'a')
errors = open('errors.txt', 'a')

async def scrap(url: str):
    temp_proxies = 0
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url, headers={'user-agent': user_agent}, 
                timeout=aiohttp.ClientTimeout(total=TIMEOUT)
            ) as response:
                html = await response.text()
                if tuple(REGEX.finditer(html)):
                    for proxy in tuple(REGEX.finditer(html)):
                        proxies.write(f'{proxy.group(1)}\n')
                        scrapped_proxies.append(proxy.group(1))
                        temp_proxies += 1
                    print(f' [~] Found: {temp_proxies} Proxies In {url}', proxy.group(1))
                else: print(f' [~] Can\'t Find At: {url}', proxy.group(1))
    except Exception as e: 
        errors.write(f'[ERROR AT]: {url} {e}\n')


async def main():
    with open('sources.txt', 'r') as sources:
        urls = sources.read().splitlines()
        await asyncio.wait(
            [ asyncio.create_task(scrap(url)) 
            for url in urls ])
        
        print(f'\n [!] Done Scraping...\n [~] Total Proxies: {len(scrapped_proxies)}')
        proxies.close()
        errors.close()


if __name__ == "__main__":
    asyncio.run(main())
