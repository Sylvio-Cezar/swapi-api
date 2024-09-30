from sqlitemodel import Model;

class Planet(Model):

    # Modelo para construção da tabela no sqlite
    def __init__(self, **kwargs):
        self.id = kwargs['id'];
        self.name = kwargs['name'];
        self.rotation_period = kwargs['rotation_period'];
        self.orbital_period = kwargs['orbital_period'];
        self.diameter = kwargs['diameter'];
        self.climate = kwargs['climate'];
        self.gravity = kwargs['gravity'];
        self.terrain = kwargs['terrain'];
        self.surface_water = kwargs['surface_water'];
        self.population = kwargs['population'];

        Model.__init__(self, self.id);
        self.getModel();

    # Especifica o nome da tabela no banco de dados
    def tablename(self):
        return 'planet';

    # Define as colunas da tabela
    def columns(self):
        return [
            {'name': 'name', 'type': 'TEXT'},
            {'name': 'rotation_period', 'type': 'TEXT'},
            {'name': 'orbital_period', 'type': 'TEXT'},
            {'name': 'diameter', 'type': 'TEXT'},
            {'name': 'climate', 'type': 'TEXT'},
            {'name': 'gravity', 'type': 'TEXT'},
            {'name': 'terrain', 'type': 'TEXT'},
            {'name': 'surface_water', 'type': 'TEXT'},
            {'name': 'population', 'type': 'TEXT'}
        ];
