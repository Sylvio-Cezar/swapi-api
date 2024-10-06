from fastapi import HTTPException;
from routes import router;
from models.starship import Starship;
import requests;

@router.get("/starships/")
def list_all_starships():
    url = 'https://swapi.dev/api/starships/';
    starships = [];

    while url:
        response = requests.get(url);
        response.raise_for_status();
        data = response.json();
        starships.extend(data['results']);
        url = data['next'];

    return starships;

def get_starship(starship_id: int):
    if starship_id < 1 or starship_id > 36:
        raise HTTPException(status_code=400, detail="ID deve ser um número entre 1 e 36.");
    
    url = f'https://swapi.dev/api/starships/{starship_id}/';
    response = requests.get(url);

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Nave não encontrada.");

    response.raise_for_status();
    starship_data = response.json();

    starship = Starship(
        id=starship_id,
        name=starship_data['name'],
        model=starship_data['model'],
        manufacturer=starship_data['manufacturer'],
        cost_in_credits=starship_data['cost_in_credits'],
        length=starship_data['length'],
        max_atmosphering_speed=starship_data['max_atmosphering_speed'],
        crew=starship_data['crew'],
        passengers=starship_data['passengers'],
        cargo_capacity=starship_data['cargo_capacity'],
        starship_class=starship_data['starship_class']
    );

    return starship;

@router.get("/starships/{starship_id}")
def get_starship_data(starship_id: int):
    return get_starship(starship_id).getData();

@router.get("/starships/{starship_id}/save")
def save_starship_data(starship_id: int):
    starship = get_starship(starship_id);
    starship.save();
    
    return f'Nave \'{starship.name}\' salva no banco de dados.';

@router.get("/starships/{starship_id}/delete")
def delete_starship_data(starship_id: int):
    starship = get_starship(starship_id);
    starship.delete();
    
    return f'Nave \'{starship.name}\' removida do banco de dados.';
