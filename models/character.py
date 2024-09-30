from sqlitemodel import Model;

class Character(Model):

    # Modelo para contrução da tabela no sqlite (ref: https://pypi.org/project/sqlitemodel/) 
    def __init__(self, **kwargs):
        self.id = kwargs['id'];
        self.name = kwargs['name'];
        self.height = kwargs['height'];
        self.mass = kwargs['mass'];
        self.hair_color = kwargs['hair_color'];
        self.skin_color = kwargs['skin_color'];
        self.eye_color = kwargs['eye_color'];
        self.birth_year = kwargs['birth_year'];
        self.gender = kwargs['gender'];

        Model.__init__(self, self.id);
        self.getModel();

    # Especifica nome da tabela no banco de dados
    def tablename(self):
        return 'character';


    # Define as colunas da tabela
    def columns(self):
        return [
            {
              'name': 'name',
              'type': 'TEXT'
            },
            {
              'name': 'height',
              'type': 'TEXT'
            },
            {
              'name': 'mass',
              'type': 'TEXT'
            },
            {
              'name': 'hair_color',
              'type': 'TEXT'
            },
            {
              'name': 'skin_color',
              'type': 'TEXT'
            },
            {
              'name': 'eye_color',
              'type': 'TEXT'
            },
            {
              'name': 'birth_year',
              'type': 'TEXT'
            },
            {
              'name': 'gender',
              'type': 'TEXT'
            }
        ];