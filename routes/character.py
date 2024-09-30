from fastapi import HTTPException;
from routes import router;
from models.character import Character
import requests;

@router.get("/characters/")
def list_all_characters():
    url = 'https://swapi.dev/api/people/';
    characters = [];
    
    while url:
        response = requests.get(url);
        response.raise_for_status();
        data = response.json();
        characters.extend(data['results']);
        url = data['next'];

    return characters;

def get_character(character_id: int):
    if character_id < 1 or character_id > 82:
        raise HTTPException(status_code=400, detail="ID deve ser um número entre 1 e 82.");
    
    url = f'https://swapi.dev/api/people/{character_id}/';
    response = requests.get(url);

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Personagem não encontrado.");
    
    response.raise_for_status();
    character_data = response.json();

    character = Character(
        id=character_id,
        name=character_data['name'],
        height=character_data['height'],
        mass=character_data['mass'],
        hair_color=character_data['hair_color'],
        skin_color=character_data['skin_color'],
        eye_color=character_data['eye_color'],
        birth_year=character_data['birth_year'],
        gender=character_data['gender']
    )

    return character;


@router.get("/characters/{character_id}")
def get_character_data(character_id: int):
    return get_character(character_id);

@router.get("/characters/{character_id}/save")
def save_character_data(character_id: int):
    character = get_character(character_id);
    character.createTable(); # Cria a tabela se não existir
    character.save();
    
    return f'Personagem \'{character.name}\' salvo no banco de dados.';

@router.get("/characters/{character_id}/delete")
def save_character_data(character_id: int):
    character = get_character(character_id);
    character.createTable(); # Cria a tabela se não existir
    character.delete();
    
    return f'Personagem \'{character.name}\' removido do banco de dados.';