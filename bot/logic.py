from os import getenv

from aiohttp import ClientSession
from pydantic import BaseModel

GET_CATS_URL = f'http://{getenv("API_HOST")}/api/random-cats'


class BreedS(BaseModel):
    id: int
    name: str


class CatS(BaseModel):
    breed: BreedS
    name: str
    description_from_owner: str


async def query_cats() -> list[CatS]:
    async with ClientSession() as session:
        async with session.get(GET_CATS_URL) as response:
            if response.status != 200:
                raise Exception('Failed to get cats')
            json = await response.json()
            return [CatS.parse_obj(cat) for cat in json]


def format_cats(cats: list[CatS]) -> str:
    html = ''
    for cat in cats:
        html += f"{cat.name}\n<strong>Breed:</strong> {cat.breed.name}\n" \
                f"<strong>Owner says:</strong> {cat.description_from_owner}\n---\n"
    return html
