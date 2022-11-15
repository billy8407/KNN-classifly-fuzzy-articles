from typing import List

from bs4 import BeautifulSoup
import requests


def get_links():
    page_links = []

    # Get All page links.
    for i in range(1, 123):
        print("Loop %d" %i)
        r = requests.get(
        "https://www.whitehouse.gov/briefing-room/speeches-remarks/page/%d/" %i
        )

        if r.status_code != 200:
            print("batch %d failed in status: %d", i, r.status_code)
            break
        
        soup = BeautifulSoup(r.text, "html.parser")
        items = soup.find_all(class_='news-item__title')
        
        for item in items:
            page_links.append(items[0]['href'])

    if i == 122:
        print('Get All page links successfully.')

    return page_links