from fastapi import FastAPI;
from routes import status, character, film, starship, vehicle, species, planet
from sqlitemodel import Database
import uvicorn;

# Define nome do arquivo para database sqlite
Database.DB_FILE = 'swapi_database.db'

app = FastAPI();

# Inclue as rotas definidas em ./routes (necessário importar cada uma)
app.include_router(status.router);
app.include_router(character.router);
app.include_router(film.router);
app.include_router(starship.router);
app.include_router(vehicle.router);
app.include_router(species.router);
app.include_router(planet.router);

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000);