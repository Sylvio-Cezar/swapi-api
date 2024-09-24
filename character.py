from fastapi import FastAPI, HTTPException;
import requests;
from pydantic import BaseModel;
from typing import List, Optional;

app = FastAPI();

class Character(BaseModel):
    name: str;
    height: str;
    mass: str;
    hair_color: str;
    skin_color: str;
    eye_color: str;
    birth_year: str;
    gender: str;

@app.get("/characters/", response_model=List[Character])
def list_all_characters():
    url = 'https://swapi.dev/api/people/';
    characters = [];
    
    while url:
        response = requests.get(url);
        response.raise_for_status();
        data = response.json();
        characters.extend(data['results']);
        url = data['next'] ;

    return characters;

@app.get("/characters/{character_id}", response_model=Character)
def get_character_data(character_id: int):
    if character_id < 1 or character_id > 82:
        raise HTTPException(status_code=400, detail="ID deve ser um número entre 1 e 82.");
    
    url = f'https://swapi.dev/api/people/{character_id}/';
    response = requests.get(url);

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail="Personagem não encontrado.");
    
    response.raise_for_status();
    character_data = response.json();
    
    return Character(
        name=character_data['name'],
        height=character_data['height'],
        mass=character_data['mass'],
        hair_color=character_data['hair_color'],
        skin_color=character_data['skin_color'],
        eye_color=character_data['eye_color'],
        birth_year=character_data['birth_year'],
        gender=character_data['gender']
    );

if __name__ == "__main__":
    import uvicorn;
    uvicorn.run(app, host="127.0.0.1", port=8000);
