from fastapi import HTTPException;
from routes import router;
from models.species import Species;
import requests;

@router.get("/species/")
def list_all_species():
    url = 'https://swapi.dev/api/species/';
    species_list = [];

    while url:
        response = requests.get(url);
        response.raise_for_status();
        data = response.json();
        species_list.extend(data['results']);
        url = data['next'];

    return species_list;

def get_species(species_id: int):
    if species_id < 1 or species_id > 37:
        raise HTTPException(status_code=400, detail="ID deve ser um número entre 1 e 37.");
    
    url = f'https://swapi.dev/api/species/{species_id}/';
    response = requests.get(url);

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Espécie não encontrada.");

    response.raise_for_status();
    species_data = response.json();

    species = Species(
        id=species_id,
        name=species_data['name'],
        classification=species_data['classification'],
        designation=species_data['designation'],
        average_height=species_data['average_height'],
        skin_colors=species_data['skin_colors'],
        hair_colors=species_data['hair_colors'],
        eye_colors=species_data['eye_colors'],
        average_lifespan=species_data['average_lifespan'],
        language=species_data['language']
    );

    return species;

@router.get("/species/{species_id}")
def get_species_data(species_id: int):
    return get_species(species_id).getData();

@router.get("/species/{species_id}/save")
def save_species_data(species_id: int):
    species = get_species(species_id);
    species.save();
    
    return f'Espécie \'{species.name}\' salva no banco de dados.';

@router.get("/species/{species_id}/delete")
def delete_species_data(species_id: int):
    species = get_species(species_id);
    species.delete();
    
    return f'Espécie \'{species.name}\' removida do banco de dados.';
