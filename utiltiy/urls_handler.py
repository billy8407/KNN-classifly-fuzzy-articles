import asyncio
import functools

from bs4 import BeautifulSoup
import requests


async def get_urls(loop, i):
    page_urls = []

    print("Get link loop %d" %i)

    # Get All page urls.
    url = "https://www.whitehouse.gov/briefing-room/speeches-remarks/page/%d/" %i
   
    
    r = await loop.run_in_executor(
        None, functools.partial(requests.get, url)
        )

    if r.status_code != 200:
        print("loop %d failed in status code : %d", i, r.status_code)
    
    # Fetch the page urls.
    soup = BeautifulSoup(r.text, "html.parser")
    items = soup.find_all(class_='news-item__title')
    page_urls: list[str] = [_['href'] for _ in items]

    return page_urls


async def urls_task():
    '''
    Use asyncio for urls crawling.
    '''

    loop = asyncio.get_event_loop()

    # Get urls from page 1 to 122.
    search_work = [get_urls(loop, i) for i in range(1, 123)]

    results: list[list[str]] = await asyncio.gather(*search_work) 

    # Use Numpy's flatten method in the list.
    urls: list[str] = [item for sublist in results for item in sublist]

    print('Get page urls finished!')

    return urls
