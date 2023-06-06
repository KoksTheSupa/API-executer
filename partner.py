import json
from urllib import request
from sw import SW


class Partner(SW):
    model_name = 'res.partner'

    def create(self):
        args = {}
        url = "https://swapi.dev/api/people"
        while url:
            data = request.urlopen(url).read()
            parsed_data = json.loads(data)
            results = parsed_data.get("results")
            for part in results:
                args['name'] = part.get('name')
                # args[f'planet'] = part.get('homeworld')
                partner_records = self.models.execute_kw(
                    self.db, self.uid, self.password, self.model_name, 'create', [args])
            url = parsed_data.get('next')


url = 'http://localhost:8069'
username = 'b@b.b'
password = 'admin'
db = 'Admin'
Partner(url, username, password, db).create()
