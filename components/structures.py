from typing import Optional

from pydantic import HttpUrl, BaseModel


# input parameters
class UrlInput(BaseModel):
    url: HttpUrl


# output parameters
class ResponseParsing(BaseModel):
    title: str
    urls: list[Optional[str]]
