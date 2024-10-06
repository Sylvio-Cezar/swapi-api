from sqlitemodel import Model;

class Species(Model):

    # Modelo para construção da tabela no sqlite
    def __init__(self, **kwargs):
        self.api_id = kwargs['id'];
        self.name = kwargs['name'];
        self.classification = kwargs['classification'];
        self.designation = kwargs['designation'];
        self.average_height = kwargs['average_height'];
        self.skin_colors = kwargs['skin_colors'];
        self.hair_colors = kwargs['hair_colors'];
        self.eye_colors = kwargs['eye_colors'];
        self.average_lifespan = kwargs['average_lifespan'];
        self.language = kwargs['language'];

        Model.__init__(self, self.api_id);
        self.createTable();
        self.getModel();

    # Especifica o nome da tabela no banco de dados
    def tablename(self):
        return 'species';

    # Define as colunas da tabela
    def columns(self):
        return [
            {'name': 'api_id', 'type': 'INTEGER PRIMARY KEY'},
            {'name': 'name', 'type': 'TEXT'},
            {'name': 'classification', 'type': 'TEXT'},
            {'name': 'designation', 'type': 'TEXT'},
            {'name': 'average_height', 'type': 'TEXT'},
            {'name': 'skin_colors', 'type': 'TEXT'},
            {'name': 'hair_colors', 'type': 'TEXT'},
            {'name': 'eye_colors', 'type': 'TEXT'},
            {'name': 'average_lifespan', 'type': 'TEXT'},
            {'name': 'language', 'type': 'TEXT'}
        ];

    def getData(self):
        return {
            "name": self.name,
            "classification": self.classification,
            "designation": self.designation,
            "average_height": self.average_height,
            "skin_colors": self.skin_colors,
            "hair_colors": self.hair_colors,
            "eye_colors": self.eye_colors,
            "average_lifespan": self.average_lifespan,
            "language": self.language
        }