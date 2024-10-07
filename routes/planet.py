from fastapi import HTTPException;
from routes import router;
from models.planet import Planet;
import requests;

@router.get("/planets/")
def list_all_planets():
    url = 'https://swapi.dev/api/planets/';
    planets = [];

    while url:
        response = requests.get(url);
        response.raise_for_status();
        data = response.json();
        planets.extend(data['results']);
        url = data['next'];

    return planets;

def get_planet(planet_id: int):
    if planet_id < 1 or planet_id > 60:
        raise HTTPException(status_code=400, detail="ID deve ser um número entre 1 e 60.");
    
    url = f'https://swapi.dev/api/planets/{planet_id}/';
    response = requests.get(url);

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Planeta não encontrado.");

    response.raise_for_status();
    planet_data = response.json();

    planet = Planet(
        id=planet_id,
        name=planet_data['name'],
        rotation_period=planet_data['rotation_period'],
        orbital_period=planet_data['orbital_period'],
        diameter=planet_data['diameter'],
        climate=planet_data['climate'],
        gravity=planet_data['gravity'],
        terrain=planet_data['terrain'],
        surface_water=planet_data['surface_water'],
        population=planet_data['population']
    );

    return planet;

@router.get("/planets/{planet_id}")
def get_planet_data(planet_id: int):
    return get_planet(planet_id).getData();

@router.get("/planets/{planet_id}/save")
def save_planet_data(planet_id: int):
    planet = get_planet(planet_id);
    planet.save();
    
    return f'Planeta \'{planet.name}\' salvo no banco de dados.';

@router.get("/planets/{planet_id}/delete")
def delete_planet_data(planet_id: int):
    planet = get_planet(planet_id);
    planet.delete();
    
    return f'Planeta \'{planet.name}\' removido do banco de dados.';
