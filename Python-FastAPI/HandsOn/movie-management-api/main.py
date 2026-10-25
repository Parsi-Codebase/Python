from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel,Field
from typing import Optional
app=FastAPI(
    title='Movie Management API',
    version='1.0.0'
)
# pydantic movie models
class Movie(BaseModel):
    title:str=Field(min_length=2)
    genre:str=Field(min_length=2)
    language:str=Field(min_length=2)
    year:int=Field(ge=1900,le=2100)
    rating:float=Field(ge=0,le=10)
class MovieUpdate(BaseModel):
    title:Optional[str]=Field(
        default=None,
        min_length=2
    )
    genre:Optional[str]=Field(
        default=None,
        min_length=2
    )
    year:Optional[int]=Field(
        default=None,
        ge=1900,
        le=2100
    )
    rating:Optional[int]=Field(
            default=None,
            ge=0,
            le=10
        )
# in memory movie data
movies = [
    {
        "id": 1,
        "title": "RRR",
        "genre": "Action",
        "language": "Telugu",
        "year": 2022,
        "rating": 8.0
    },
    {
        "id": 2,
        "title": "Baahubali",
        "genre": "Action",
        "language": "Telugu",
        "year": 2015,
        "rating": 8.0
    },
    {
        "id": 3,
        "title": "3 Idiots",
        "genre": "Comedy",
        "language": "Hindi",
        "year": 2009,
        "rating": 8.4
    }
]
# get all movies
@app.get('/movies')
def get_movies():
    return movies
# get movie by id
@app.get('/movies/{movie_id}')
def get_movie(movie_id:int):
    for movie in movies:
        if movie['id']==movie_id:
            return movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Movie not found'
    )
# post-Create Movie
@app.post('/movies',
          status_code=status.HTTP_201_CREATED)
def create_movie(movie:Movie):
    # generate new Id
    new_id=max([m['id'] for m in movies],default=0)+1
    new_movie={
     'id':new_id,
     'title':movie.title,
     'genre':movie.genre,
     'language':movie.language,
     'year':movie.year,
     'rating':movie.rating   
    }
    movies.append(new_movie)
    return new_movie
        
# put-update complete movie
@app.put('/movies/{movie_id}')
def update_movie(
    movie_id:int,
    movie:Movie
):
    for existing_movie in movies:
        if existing_movie['id']==movie_id:
            existing_movie['title']=movie.title
            existing_movie["genre"] = movie.genre
            existing_movie["language"] = movie.language
            existing_movie["year"] = movie.year
            existing_movie["rating"] = movie.rating

            return existing_movie

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Movie not found"
    )
#patch -Partial Update
@app.patch('/movies/{movie_id}')
def patch_movie(
    movie_id:int,
    movie:MovieUpdate
):
    for existing_movie in movies:
        if existing_movie['id']==movie_id:
            update_data=movie.model_dump(
                exclude_unset=True
            )
            existing_movie.update(update_data)
            return existing_movie
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='movie not found'
    )
# delete movie
@app.delete('/movies/{movie_id}')
def delete_movie(movie_id:int):
    for movie in movies:
        if movie['id']==movie_id:
            movies.remove(movie)
            return{
                'message':'movie deleted successfully'
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="movie not found"
    )