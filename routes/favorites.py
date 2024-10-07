from routes import router;
from models.favorite import Favorite;
from sqlitemodel import SQL;
from routes import character, film, starship, vehicle, species, planet;

@router.get("/favorites")
def list_all_favorites():
    sql = SQL().SELECT('*').FROM('favorite');
    favorites = Favorite().select(sql);
    favorites_data = [];
    for favorite in favorites:
        favorites_data.append(favorite.getData())
    return favorites_data;

@router.get("/favorites/save")
def save_favorite_data():
    favorite1_definitions = {
        "id": 1,
        "character": character.get_character(20),
        "film": film.get_film(2),
        "starship": starship.get_starship(2),
        "vehicle": vehicle.get_vehicle(4),
        "specie": species.get_species(6),
        "planet": planet.get_planet(3),
        "student": {
            "name": "Jean Arthur",
            "ra": 98021538,
            "course": "Sistemas de Informação",
            "university": "Univás - Universidade do Vale do Sapucaí",
            "period": 6
        }
    };
    
    favorite1 = Favorite(
        id=favorite1_definitions['id'],
        character_name=favorite1_definitions['character'].name,
        character_birth_year=favorite1_definitions['character'].birth_year,
        film_title=favorite1_definitions['film'].title,
        film_episode_id=favorite1_definitions['film'].episode_id,
        starship_name=favorite1_definitions['starship'].name,
        starship_model=favorite1_definitions['starship'].model,
        vehicle_name=favorite1_definitions['vehicle'].name,
        vehicle_model=favorite1_definitions['vehicle'].model,
        specie_homeworld=favorite1_definitions['specie'].homeworld,
        specie_language=favorite1_definitions['specie'].language,
        planet_name=favorite1_definitions['planet'].name,
        planet_population=favorite1_definitions['planet'].population,
        student_name=favorite1_definitions['student']['name'],
        student_ra=favorite1_definitions['student']['ra'],
        student_course=favorite1_definitions['student']['course'],
        student_university=favorite1_definitions['student']['university'],
        student_period=favorite1_definitions['student']['period']
    );

    favorite1.save();
    
    return f'Favoritos de \'{favorite1.student_name}\' e \'{"A DEFINIR"}\' salvo no banco de dados.';