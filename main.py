from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class GenreURLChoices(Enum):
    ROCK = 'rock'
    METAL = 'metal'
    PROGRESSIVE_ROCK = 'progressive rock'
    HARD_ROCK = 'hard rock'
    GRUNGE = 'grunge'


# Fixed the BANDS dictionary syntax and added more bands
BANDS = [
    {'id': 1, 'name': 'The Beatles', 'genre': 'Rock', 'country': 'UK'},
    {'id': 2, 'name': 'Queen', 'genre': 'Rock', 'country': 'UK'},
    {'id': 3, 'name': 'Metallica', 'genre': 'Metal', 'country': 'USA'},
    {'id': 4, 'name': 'Pink Floyd', 'genre': 'Progressive Rock', 'country': 'UK'},
    {'id': 5, 'name': 'AC/DC', 'genre': 'Hard Rock', 'country': 'Australia'},
    {'id': 6, 'name': 'Led Zeppelin', 'genre': 'Rock', 'country': 'UK'},
    {'id': 7, 'name': 'Nirvana', 'genre': 'Grunge', 'country': 'USA'},
]


@app.get("/")    
async def index() -> dict[str, str]:
    return {"message": "Hello World"}

# get all bands
@app.get("/bands", status_code=200, response_model=dict) 
async def get_bands() :
    return {"bands": BANDS}

# get a specific band by ID
@app.get("/bands/{band_id}", status_code=200, response_model=dict) 
async def get_band(band_id: int) -> dict:
    for band in BANDS:
        if band["id"] == band_id:
            return band
    return HTTPException(status_code=404, detail="Band not found")

# get bands by genre
@app.get("/bands/genre/{genre}", status_code=200, response_model=dict)
async def get_bands_by_genre(genre: GenreURLChoices) -> dict:
    return {"bands": [band for band in BANDS if band["genre"].lower() == genre.value.lower()]}