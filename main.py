import asyncio

from utiltiy.links_handler import links_task


def download_data():
    page_links = asyncio.run(
        links_task()
    )
    pass

if __name__ == '__main__':
    download_data()