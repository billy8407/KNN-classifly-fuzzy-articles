import asyncio

from utiltiy.content_handler import content_task
from utiltiy.file_handler import File
from utiltiy.urls_handler import urls_task


def download_data():
    # All pages's urls
    urls = asyncio.run(
        urls_task()
    )
    
    # Keep urls in a file.
    File.write_json('urls.json', urls)
    
    r = asyncio.run(
        content_task(urls)
    )


if __name__ == '__main__':
    download_data()
