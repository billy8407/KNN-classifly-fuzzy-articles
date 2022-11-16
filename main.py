import asyncio

from utiltiy.content_handler import article_task
from utiltiy.file_handler import File
from utiltiy.urls_handler import urls_task


def download_data():
    # All pages's urls
    urls = asyncio.run(
        urls_task()
    )
    
    # Keep urls in a file.
    File.write_json('urls.json', urls)
    
    articles = asyncio.run(
        article_task(urls)
    )


if __name__ == '__main__':
    download_data()
