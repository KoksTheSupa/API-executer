import json
from urllib import request
from sw import SW


class Planet(SW):
    model_name = 'res.planet'

    def check_int(self, variable, pedastrian):
        if isinstance(variable, int):
            variable = pedastrian
        else:
            variable = 0

    def create(self):
        args = {}
        args['diameter'] = 0
        args['rotation_period'] = 0
        args['orbital_period'] = 0
        url = "https://swapi.dev/api/planets"
        while url:
            data = request.urlopen(url).read()
            parsed_data = json.loads(data)
            results = parsed_data.get("results")
            for part in results:
                args['name'] = part.get('name')
                self.check_int(args['rotation_period'],
                               part.get('rotation_period'))
                self.check_int(args['diameter'], part.get('diameter'))
                self.check_int(args['orbital_period'],
                               part.get('orbital_period'))
                args['population'] = part.get('population')
                self.models.execute_kw(
                    self.db, self.uid, self.password, self.model_name, 'create', [args])
            url = parsed_data.get('next')


url = 'http://localhost:8069'
username = 'b@b.b'
password = 'admin'
db = 'Admin'
Planet(url, username, password, db).create()
