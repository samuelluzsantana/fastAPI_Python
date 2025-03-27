from fastapi import FastAPI
from schemas import GenreURLChoices, Band 

app = FastAPI()

# Fixed the BANDS dictionary syntax and added more bands
BANDS = [
    {'id': 1, 'name': 'The Beatles', 'genre': 'rock', 'country': 'UK'},
    {'id': 2, 'name': 'Queen', 'genre': 'rock', 'country': 'UK'},
    {'id': 3, 'name': 'Metallica', 'genre': 'metal', 'country': 'USA'},
    {'id': 4, 'name': 'Pink Floyd', 'genre': 'progressive rock', 'country': 'UK'},
    {'id': 5, 'name': 'AC/DC', 'genre': 'hard rock', 'country': 'Australia', 'albums': {'title': 'Back in Black', 'release_date': '1980-07-25'}},
    {'id': 6, 'name': 'Led Zeppelin', 'genre': 'rock', 'country': 'UK', 'albums': [{'title': 'Led Zeppelin IV', 'release_date': '1971-11-08'}]},
    {'id': 7, 'name': 'Nirvana', 'genre': 'grunge', 'country': 'USA'},
]


@app.get("/")    
async def index() -> dict[str, str]:
    return {"message": "Hello World"}

# get all bands
@app.get("/bands", status_code=200, response_model=list[Band]) 
async def get_bands() -> list[Band]:
    return [
        Band(**band) for band in BANDS
    ]

# get a specific band by ID
@app.get("/bands/{band_id}", status_code=200, response_model=Band) 
async def get_band(band_id: int) -> Band:
    for band in BANDS:
        if band["id"] == band_id:
            return band
    return HTTPException(status_code=404, detail="Band not found")

# get bands by genre
@app.get("/bands/genre/{genre}", response_model=list[Band])
async def get_bands_by_genre(genre: GenreURLChoices) -> list[Band]:
        return [Band(**band) for band in BANDS if band["genre"] == genre.value]