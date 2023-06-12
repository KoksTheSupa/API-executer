from base64 import b64encode
from itertools import chain
from urllib import request, error
import json
import yaml

from script.log import logger


class YAMLReader():
    def read_yaml(self, file_path):
        """Read yaml file"""
        with open(file_path) as stream:
            return yaml.safe_load(stream)

    def check_path(self):
        """Check valid path"""
        configure_path = input('Enter a configure file path: ')
        try:
            self.read_yaml(configure_path)
        except FileNotFoundError:
            print("Please check correct path")
            return False
        print("Program has been started...")
        return configure_path


yaml_reader = YAMLReader()


class Validator:

    def check_int(self, variable):
        """Check value is int"""
        try:
            int(variable)
        except ValueError:
            variable = 0
        return variable


validator = Validator()


class SWAPI():
    def __init__(self, url):
        self._url = url

    def get_data(self):
        """Get data from url"""
        data = request.urlopen(self._url).read()
        return json.loads(data)

    def parse_data(self):
        """Parse data"""
        results = []
        while self._url:
            data = self.get_data()
            result = data.get("results")
            results.append(result)
            self._url = data.get('next')
        res = list(chain(*results))
        return res


class ImageAPI():
    def __init__(self, image_url):
        self._image_url = image_url

    def get_image(self):
        """Get decode image data && check valid url"""
        try:
            image = request.urlopen(self._image_url).read()
        except error.HTTPError:
            return False
        encoded_image = b64encode(image)
        return encoded_image.decode('ascii')

    def get_list_image(self, length):
        """Get list of image for Partner"""
        image_list = []
        id = 1
        image_url = f"https://starwars-visualguide.com/assets/img/characters/{id}.jpg"
        while len(image_list) < length:
            image = ImageAPI(image_url).get_image()
            id += 1
            if not image:
                logger.warning(
                    f"Oops, cant get image {image_url}, for correct display skip this url")
                image_url = f"https://starwars-visualguide.com/assets/img/characters/{id}.jpg"
                continue
            image_url = f"https://starwars-visualguide.com/assets/img/characters/{id}.jpg"
            image_list.append(image)
        return image_list
