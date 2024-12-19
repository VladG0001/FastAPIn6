from typing import Optional

from pydantic import HttpUrl, BaseModel


class UrlInput(BaseModel):
    url: HttpUrl


class ResponseParsing(BaseModel):
    title: str
    urls: list[Optional[str]]
