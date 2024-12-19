from fastapi import FastAPI, Query
import uvicorn
from components.structures import UrlInput, ResponseParsing
from components.tools import get_html, parsing_get_title_a, get_data
from bs4 import BeautifulSoup

# Створюємо додаток FastAPI
app = FastAPI()


# Створюємо асинхронний ендпоінт для отримання інформації з URL
@app.get("/info-url")
async def parsing_url(url_inp: UrlInput = Query(..., description="введіть URL для парсингу")
                      ) -> ResponseParsing:
    # Отримуємо HTML-дані з переданого URL
    html_data = await get_html(str(url_inp.url))

    # Парсимо заголовок та всі URL-адреси з HTML
    title_of_soup, urls_of_soup = await parsing_get_title_a(html_data)

    # Повертаємо результат у вигляді об'єкту ResponseParsing
    return ResponseParsing(title=title_of_soup, urls=urls_of_soup)


@app.get("/wiki/data_program")
async def parsing_url():
    pass


# Запуск програми з використанням uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
