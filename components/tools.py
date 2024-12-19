import httpx
from fastapi.exceptions import HTTPException
from bs4 import BeautifulSoup


# Асинхронна функція для отримання HTML-даних з веб-сторінки за допомогою httpx
async def get_html(url) -> str:
    async with httpx.AsyncClient() as client:
        # Надсилаємо запит GET до URL
        response = await client.get(url)

        # Перевіряємо, чи статус відповіді не є 200 (OK), якщо ні — викликаємо помилку 404
        if response.status_code != 200:
            raise HTTPException(404, detail=f"некоректний url: {url}: код статусу={response.status_code}")

        # Перевіряємо, чи контент є HTML, якщо ні — викликаємо помилку 404
        elif 'text/html' not in response.headers['content-type']:
            raise HTTPException(404, detail=f"некоректний тип контенту: {url}: {response.headers['content-type']}")

        # Повертаємо HTML-текст у вигляді рядка
        return response.text


# Асинхронна функція для парсингу заголовка сторінки (title) та всіх URL-адрес (a) з HTML-даних
async def parsing_get_title_a(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')

    # Отримуємо текст заголовка сторінки
    title_of_soup = soup.title.text

    # Отримуємо список всіх URL-адрес зі сторінки
    urls_of_soup = [link.get('href') for link in soup.find_all('a')]

    # Повертаємо заголовок та URL-адреси
    return title_of_soup, urls_of_soup


# Функція для отримання певних даних з таблиці на сторінці
def get_data(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')

    # Знаходимо таблицю з класом "infobox"
    info_table = soup.find("table", class_="infobox")

    # Знаходимо рядок з текстом "Парадигма"
    paradigm = info_table.find("th", text="Парадигма")

    # Отримуємо текст сусідньої комірки з інформацією про парадигму
    data_paradigm = paradigm.next_sibling.text

    return {"paradigma": data_paradigm}
