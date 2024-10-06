from sqlitemodel import Model;

class Starship(Model):

    # Modelo para construção da tabela no sqlite
    def __init__(self, **kwargs):
        self.api_id = kwargs['id'];
        self.name = kwargs['name'];
        self.model = kwargs['model'];
        self.manufacturer = kwargs['manufacturer'];
        self.cost_in_credits = kwargs['cost_in_credits'];
        self.length = kwargs['length'];
        self.max_atmosphering_speed = kwargs['max_atmosphering_speed'];
        self.crew = kwargs['crew'];
        self.passengers = kwargs['passengers'];
        self.cargo_capacity = kwargs['cargo_capacity'];
        self.starship_class = kwargs['starship_class'];

        Model.__init__(self, self.api_id);
        self.createTable();
        self.getModel();

    # Especifica nome da tabela no banco de dados
    def tablename(self):
        return 'starship';

    # Define as colunas da tabela
    def columns(self):
        return [
            {'name': 'api_id', 'type': 'INTEGER PRIMARY KEY'},
            {'name': 'name', 'type': 'TEXT'},
            {'name': 'model', 'type': 'TEXT'},
            {'name': 'manufacturer', 'type': 'TEXT'},
            {'name': 'cost_in_credits', 'type': 'TEXT'},
            {'name': 'length', 'type': 'TEXT'},
            {'name': 'max_atmosphering_speed', 'type': 'TEXT'},
            {'name': 'crew', 'type': 'TEXT'},
            {'name': 'passengers', 'type': 'TEXT'},
            {'name': 'cargo_capacity', 'type': 'TEXT'},
            {'name': 'starship_class', 'type': 'TEXT'}
        ];

    def getData(self):
        return {
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "starship_class": self.starship_class
        }