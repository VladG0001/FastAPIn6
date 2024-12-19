import httpx
from fastapi.exceptions import HTTPException
from bs4 import BeautifulSoup


async def get_html(url) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code != 200:
            raise HTTPException(404, detail=f"некоректний url: {url}: код статусу={response.status_code}")

        elif 'text/html' not in response.headers['content-type']:
            raise HTTPException(404, detail=f"некоректний тип контенту: {url}: {response.headers['content-type']}")

        return response.text


async def parsing_get_title_a(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')

    title_of_soup = soup.title.text

    urls_of_soup = [link.get('href') for link in soup.find_all('a')]

    return title_of_soup, urls_of_soup


def get_data(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')

    info_table = soup.find("table", class_="infobox")

    paradigm = info_table.find("th", text="Парадигма")

    data_paradigm = paradigm.next_sibling.text

    return {"paradigma": data_paradigm}
