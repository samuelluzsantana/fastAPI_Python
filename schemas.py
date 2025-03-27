from datetime import date
from enum import Enum
from pydantic import BaseModel


class GenreURLChoices(Enum):
    ROCK = 'rock'
    METAL = 'metal'
    PROGRESSIVE_ROCK = 'progressive rock'
    HARD_ROCK = 'hard rock'
    GRUNGE = 'grunge'


class Album(BaseModel):
    title: str
    release_date: date
    
class Band(BaseModel):
    id: int
    name: str
    genre: GenreURLChoices
    country: str
    albums: list[Album] = []