import asyncio

from utiltiy.file_handler import File
from utiltiy.links_handler import links_task


def download_data():
    # All pages's urls
    links = asyncio.run(
        links_task()
    )
    
    # Keep urls in a file.
    File.write_json('links.json', links)
    

if __name__ == '__main__':
    download_data()
