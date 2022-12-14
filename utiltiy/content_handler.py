import asyncio
import functools
import re

from bs4 import BeautifulSoup
import requests


async def get_article(loop, url):    
    r = await loop.run_in_executor(
            None, functools.partial(requests.get, url)
        )
    
    soup = BeautifulSoup(r.text, "html.parser")

    # Point to tag "article" and get all tag "p" content.
    content_blocks: list[object] = soup.find('article').find_all('p')
    
    article = {}

    # Fetch title from url.
    match = re.match(r".*/(.*)/", url)
    title = match.group(1).replace('-', ' ') 

    paragraph = []

    for content_block in content_blocks:
        content: str = re.sub("\(\w*\.?\)", '', content_block.text)

        if '\xa0' in content:
            sentences: list = content.split("\xa0")
            '''
            if '' in sentences:
                sentences.remove('')
            if ' ' in sentences:
                sentences.remove(' ')
            '''

            paragraph += sentences
        else:
            paragraph.append(content) 

    # Classify articles to three categoris by title.
        if 'biden' in title and 'harris' not in title:
            # 'biden' tag in 0
            category = 0
        elif 'harris' in title and 'biden' not in title:
            # 'harris' tag in 1
            category = 'harris'
        else:
            # 'fuzzy' tag in 2
            category = 'fuzzy'

    article['title'] = title
    article['category'] = category

    # Join an article's all paragraph and sentences to one string.
    article['content'] = '\n'.join(paragraph)

    return article


async def article_task(urls: list):
    '''
    Use asyncio for content crawling.
    '''

    loop = asyncio.get_event_loop()

    # Get urls from page 1 to 122.
    search_work = [get_article(loop, url) for url in urls]

    print('Fetching urls from page 1 to 122 ...')
    articles: list[list[str]] = await asyncio.gather(*search_work) 


    print('Get %d articles finished!' %len(articles))

    return articles
