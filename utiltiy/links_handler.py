import asyncio
import functools

from bs4 import BeautifulSoup
import requests


async def get_links(loop, i):
    page_links = []

    print("Get link loop %d" %i)

    # Get All page links.
    url = "https://www.whitehouse.gov/briefing-room/speeches-remarks/page/%d/" %i
   
    
    r = await loop.run_in_executor(
        None, functools.partial(requests.get, url)
        )

    if r.status_code != 200:
        print("loop %d failed in status code : %d", i, r.status_code)
    
    # Fetch link
    soup = BeautifulSoup(r.text, "html.parser")
    items = soup.find_all(class_='news-item__title')
    page_link: str = items[0]['href']

    return page_link


async def links_task():
    '''
    Use asyncio for links crawling.
    '''
    
    loop = asyncio.get_event_loop()

    # Get links from page 1 to 122.
    search_work = [get_links(loop, i) for i in range(1, 123)]

    page_links: list = await asyncio.gather(*search_work)   
    
    print('Get page links finished!')

    return page_links
