from sqlitemodel import Model;

class Film(Model):

    # Modelo para construção da tabela no sqlite
    def __init__(self, **kwargs):
        self.api_id = kwargs['id'];
        self.title = kwargs['title'];
        self.episode_id = kwargs['episode_id'];
        self.opening_crawl = kwargs['opening_crawl'];
        self.director = kwargs['director'];
        self.producer = kwargs['producer'];
        self.release_date = kwargs['release_date'];

        Model.__init__(self, self.api_id);
        self.createTable();
        self.getModel();

    # Especifica nome da tabela no banco de dados
    def tablename(self):
        return 'film';

    # Define as colunas da tabela
    def columns(self):
        return [
            {'name': 'api_id', 'type': 'INTEGER PRIMARY KEY'},
            {'name': 'title', 'type': 'TEXT'},
            {'name': 'episode_id', 'type': 'INTEGER'},
            {'name': 'opening_crawl', 'type': 'TEXT'},
            {'name': 'director', 'type': 'TEXT'},
            {'name': 'producer', 'type': 'TEXT'},
            {'name': 'release_date', 'type': 'TEXT'}
        ];

    def getData(self):
        return {
            "title": self.title,
            "episode_id": self.episode_id,
            "opening_crawl": self.opening_crawl,
            "director": self.director,
            "producer": self.producer,
            "release_date": self.release_date
        }