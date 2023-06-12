from abc import ABC, abstractmethod

from script.client import odoo_client
from script.log import logger
from script.utils import SWAPI, validator, ImageAPI


class Model(ABC):
    def __init__(self, model_name, api_url):
        self._model_name = model_name
        self.client = odoo_client
        self.results = SWAPI(api_url).parse_data()
        self.args = []

    @abstractmethod
    def get_args(self):
        """Get arguments for model"""
        pass


class OdooPlanet(Model):
    def get_args(self):
        """Get arguments for Planet model"""
        id = 1
        for part in self.results:
            arg = {}
            arg['name'] = part.get('name')
            odoo_id = self.client.get_odoo_id(self._model_name, arg['name'])
            if odoo_id:
                logger.info(
                    f"Oops, In {self._model_name} already created {arg['name']} odoo_id: {odoo_id}")
                continue
            arg['rotation_period'] = validator.check_int(
                part.get('rotation_period'))
            arg['diameter'] = validator.check_int(part.get('diameter'))
            arg['orbital_period'] = validator.check_int(
                part.get('orbital_period'))
            arg['population'] = part.get('population')
            logger.info(
                f"Args have been received to {self._model_name}: {arg['name']} id:{id}")
            id += 1
            self.args.append(arg)
        return self.args


class OdooPartner(Model):

    def get_args(self, image_url):
        """Get arguments for Partner model"""
        id = 0
        image_list = ImageAPI(image_url).get_list_image(len(self.results))
        for part in self.results:
            arg = {}
            arg['name'] = part.get('name')
            id_partner = self.client.get_odoo_id(self._model_name, arg['name'])
            if id_partner:
                logger.info(
                    f"Oops, In {self._model_name} already created {arg['name']} odoo_id: {id_partner}")
                continue
            arg['image_1920'] = image_list[id]
            parsed_planet = SWAPI(part.get('homeworld')).get_data()
            name_planet = parsed_planet.get("name")
            id_planet = self.client.get_odoo_id(self._model_name, name_planet)
            arg['planet'] = "".join(map(str, id_planet))
            logger.info(
                f"Args have been received to {self._model_name}: {arg['name']} id:{id + 1}")
            id += 1
            self.args.append(arg)
        return self.args
