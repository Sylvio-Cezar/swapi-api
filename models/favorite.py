from sqlitemodel import Model;

class Favorite(Model):

    def __init__(self):
        Model.__init__(self);

    # Modelo para construção da tabela no sqlite
    def __init__(self, **kwargs):
        try:
            self.fav_id = kwargs['id'];
            self.character_name = kwargs['character_name'];
            self.character_birth_year = kwargs['character_birth_year'];
            self.film_title = kwargs['film_title'];
            self.film_episode_id = kwargs['film_episode_id'];
            self.starship_name = kwargs['starship_name'];
            self.starship_model = kwargs['starship_model'];
            self.vehicle_name = kwargs['vehicle_name'];
            self.vehicle_model = kwargs['vehicle_model'];
            self.specie_homeworld = kwargs['specie_homeworld'];
            self.specie_language = kwargs['specie_language'];
            self.planet_name = kwargs['planet_name'];
            self.planet_population = kwargs['planet_population'];
            self.student_name = kwargs['student_name'];
            self.student_ra = kwargs['student_ra'];
            self.student_course = kwargs['student_course'];
            self.student_university = kwargs['student_university'];
            self.student_period = kwargs['student_period'];

            Model.__init__(self, self.fav_id);
        except KeyError:
            Model.__init__(self);

        self.createTable();
        self.getModel();

    # Especifica nome da tabela no banco de dados
    def tablename(self):
        return 'favorite';

    # Define as colunas da tabela
    def columns(self):
        return [
            {'name': 'fav_id', 'type': 'INTEGER PRIMARY KEY'},
            {'name': 'character_name', 'type': 'TEXT'},
            {'name': 'character_birth_year', 'type': 'TEXT'},
            {'name': 'film_title', 'type': 'TEXT'},
            {'name': 'film_episode_id', 'type': 'INTEGER'},
            {'name': 'starship_name', 'type': 'TEXT'},
            {'name': 'starship_model', 'type': 'TEXT'},
            {'name': 'vehicle_name', 'type': 'TEXT'},
            {'name': 'vehicle_model', 'type': 'TEXT'},
            {'name': 'specie_homeworld', 'type': 'TEXT'},
            {'name': 'specie_language', 'type': 'TEXT'},
            {'name': 'planet_name', 'type': 'TEXT'},
            {'name': 'planet_population', 'type': 'TEXT'},
            {'name': 'student_name', 'type': 'TEXT'},
            {'name': 'student_ra', 'type': 'TEXT'},
            {'name': 'student_course', 'type': 'TEXT'},
            {'name': 'student_university', 'type': 'TEXT'},
            {'name': 'student_period', 'type': 'TEXT'}
        ];

    def getData(self):
        return {
            "character_name": self.character_name,
            "character_birth_year": self.character_birth_year,
            "film_title": self.film_title,
            "film_episode_id": self.film_episode_id,
            "starship_name": self.starship_name,
            "starship_model": self.starship_model,
            "vehicle_name": self.vehicle_name,
            "vehicle_model": self.vehicle_model,
            "specie_homeworld": self.specie_homeworld,
            "specie_language": self.specie_language,
            "planet_name": self.planet_name,
            "planet_population": self.planet_population,
            "student_name": self.student_name,
            "student_ra": self.student_ra,
            "student_course": self.student_course,
            "student_university": self.student_university,
            "student_period": self.student_period
        }