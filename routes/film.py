from fastapi import HTTPException;
from routes import router;
from models.film import Film;
import requests;

@router.get("/films/")
def list_all_films():
    url = 'https://swapi.dev/api/films/';
    films = [];

    while url:
        response = requests.get(url);
        response.raise_for_status();
        data = response.json();
        films.extend(data['results']);
        url = data['next'];

    return films;

def get_film(film_id: int):
    if film_id < 1 or film_id > 6:
        raise HTTPException(status_code=400, detail="ID deve ser um número entre 1 e 6.");
    
    url = f'https://swapi.dev/api/films/{film_id}/';
    response = requests.get(url);

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Filme não encontrado.");

    response.raise_for_status();
    film_data = response.json();

    film = Film(
        id=film_id,
        title=film_data['title'],
        episode_id=film_data['episode_id'],
        opening_crawl=film_data['opening_crawl'],
        director=film_data['director'],
        producer=film_data['producer'],
        release_date=film_data['release_date']
    );

    return film;

@router.get("/films/{film_id}")
def get_film_data(film_id: int):
    return get_film(film_id);

@router.get("/films/{film_id}/save")
def save_film_data(film_id: int):
    film = get_film(film_id);
    film.createTable();  # Cria a tabela se não existir
    film.save();
    
    return f'Filme \'{film.title}\' salvo no banco de dados.';

@router.get("/films/{film_id}/delete")
def delete_film_data(film_id: int):
    film = get_film(film_id);
    film.createTable();  # Cria a tabela se não existir
    film.delete();
    
    return f'Filme \'{film.title}\' removido do banco de dados.';
